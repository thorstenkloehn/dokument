use std::collections::BTreeMap;
use std::fs;
use std::path::{Path, PathBuf};

use anyhow::{bail, Context, Result};
use clap::Parser;
use serde::Deserialize;

/// Konvertiert die Struktur einer mkdocs.yml (nav + Metadaten) in ein mdBook-Projekt
/// (book.toml + src/SUMMARY.md) und kopiert den Docs-Inhalt unverändert nach src/.
#[derive(Parser)]
#[command(version, about)]
struct Args {
    /// Pfad zur mkdocs.yml
    #[arg(long, default_value = "mkdocs.yml")]
    config: PathBuf,

    /// Pfad zum docs/-Verzeichnis
    #[arg(long, default_value = "docs")]
    docs: PathBuf,

    /// Zielverzeichnis für das mdBook-Projekt
    #[arg(long, default_value = "mdbook-out")]
    output: PathBuf,
}

#[derive(Deserialize)]
struct MkdocsConfig {
    site_name: Option<String>,
    site_description: Option<String>,
    #[serde(default)]
    theme: Theme,
    nav: Vec<serde_yaml::Value>,
}

#[derive(Deserialize, Default)]
struct Theme {
    language: Option<String>,
}

enum NavNode {
    Leaf { title: String, path: String },
    Section { title: String, children: Vec<NavNode> },
}

fn parse_nav_item(value: &serde_yaml::Value) -> Result<NavNode> {
    if let Some(path) = value.as_str() {
        let title = Path::new(path)
            .file_stem()
            .map(|s| s.to_string_lossy().to_string())
            .unwrap_or_else(|| path.to_string());
        return Ok(NavNode::Leaf { title, path: path.to_string() });
    }

    let mapping = value
        .as_mapping()
        .with_context(|| format!("Ungültiger nav-Eintrag (weder String noch Mapping): {value:?}"))?;

    if mapping.len() != 1 {
        bail!("nav-Eintrag muss genau einen Schlüssel haben, gefunden: {}", mapping.len());
    }

    let (key, val) = mapping.iter().next().unwrap();
    let title = key
        .as_str()
        .with_context(|| format!("nav-Titel ist kein String: {key:?}"))?
        .to_string();

    if let Some(path) = val.as_str() {
        return Ok(NavNode::Leaf { title, path: path.to_string() });
    }

    if let Some(seq) = val.as_sequence() {
        let children = seq.iter().map(parse_nav_item).collect::<Result<Vec<_>>>()?;
        return Ok(NavNode::Section { title, children });
    }

    bail!("nav-Wert für '{title}' ist weder Pfad noch Liste: {val:?}");
}

fn escape_title(title: &str) -> String {
    title.replace('[', r"\[").replace(']', r"\]")
}

fn write_nav_node(
    node: &NavNode,
    depth: usize,
    docs_dir: &Path,
    out: &mut String,
    missing: &mut Vec<String>,
) {
    let indent = "    ".repeat(depth);
    match node {
        NavNode::Leaf { title, path } => {
            if !docs_dir.join(path).is_file() {
                missing.push(path.clone());
            }
            out.push_str(&format!("{indent}- [{}]({})\n", escape_title(title), path));
        }
        NavNode::Section { title, children } => {
            // mdBook unterstützt Draft-Kapitel (Titel ohne Link) für reine Gruppierungsknoten,
            // wie sie mkdocs-nav-Sektionen ohne eigene Seite häufig sind.
            out.push_str(&format!("{indent}- [{}]()\n", escape_title(title)));
            for child in children {
                write_nav_node(child, depth + 1, docs_dir, out, missing);
            }
        }
    }
}

fn copy_dir_recursive(src: &Path, dst: &Path) -> Result<()> {
    fs::create_dir_all(dst)?;
    for entry in fs::read_dir(src).with_context(|| format!("kann {} nicht lesen", src.display()))? {
        let entry = entry?;
        let file_type = entry.file_type()?;
        let target = dst.join(entry.file_name());
        if file_type.is_dir() {
            copy_dir_recursive(&entry.path(), &target)?;
        } else {
            fs::copy(entry.path(), &target)
                .with_context(|| format!("kann {} nicht kopieren", entry.path().display()))?;
        }
    }
    Ok(())
}

/// Sucht mkdocs/Material-spezifische Syntax, die mdBook ohne Preprocessor nicht versteht,
/// und meldet sie als Hinweis (keine automatische Umschreibung, um Inhalte nicht zu beschädigen).
fn scan_incompatible_syntax(root: &Path) -> Result<BTreeMap<String, Vec<(usize, &'static str)>>> {
    let mut findings: BTreeMap<String, Vec<(usize, &'static str)>> = BTreeMap::new();
    scan_dir(root, root, &mut findings)?;
    Ok(findings)
}

/// Prüft, ob `candidate` (Text zwischen zwei ':'-Zeichen) ein Material/pymdownx.emoji
/// Icon-Shortcode ist, z.B. "material-robot" aus ":material-robot:".
fn is_icon_shortcode(candidate: &str) -> bool {
    const PREFIXES: [&str; 4] = ["material-", "fontawesome-", "octicons-", "simple-"];
    if candidate.is_empty() || candidate.len() > 60 {
        return false;
    }
    if !candidate.chars().all(|c| c.is_ascii_lowercase() || c.is_ascii_digit() || c == '-') {
        return false;
    }
    PREFIXES.iter().any(|p| candidate.starts_with(p))
}

/// Sucht in einer Zeile nach Icon-Shortcodes zwischen ':'-Zeichen. Betrachtet jeden
/// Abschnitt zwischen zwei aufeinanderfolgenden ':' als Kandidaten (unabhängig von
/// gerader/ungerader Position), damit auch mehrere Shortcodes pro Zeile erkannt werden.
fn line_has_icon_shortcode(line: &str) -> bool {
    let parts: Vec<&str> = line.split(':').collect();
    if parts.len() < 3 {
        return false;
    }
    parts[1..parts.len() - 1].iter().any(|c| is_icon_shortcode(c))
}

fn scan_dir(
    root: &Path,
    dir: &Path,
    findings: &mut BTreeMap<String, Vec<(usize, &'static str)>>,
) -> Result<()> {
    for entry in fs::read_dir(dir)? {
        let entry = entry?;
        let path = entry.path();
        if entry.file_type()?.is_dir() {
            scan_dir(root, &path, findings)?;
            continue;
        }
        if path.extension().and_then(|e| e.to_str()) != Some("md") {
            continue;
        }
        let content = fs::read_to_string(&path).unwrap_or_default();
        let rel = path.strip_prefix(root).unwrap_or(&path).to_string_lossy().to_string();
        for (i, line) in content.lines().enumerate() {
            let trimmed = line.trim_start();
            let mut hits: Vec<&'static str> = Vec::new();
            if trimmed.starts_with("!!! ") || trimmed.starts_with("???") {
                hits.push("Material-Admonition (!!!/???) — mdBook braucht z.B. mdbook-admonish");
            } else if trimmed.starts_with("=== ") {
                hits.push("pymdownx.tabbed-Tab — mdBook braucht z.B. mdbook-tabs");
            }
            if line_has_icon_shortcode(line) {
                hits.push(
                    "Material-Icon-Shortcode (:material-…:/:fontawesome-…:/:octicons-…:/:simple-…:) — mdBook rendert das nicht, Text bleibt wörtlich stehen",
                );
            }
            for reason in hits {
                findings.entry(rel.clone()).or_default().push((i + 1, reason));
            }
        }
    }
    Ok(())
}

fn main() -> Result<()> {
    let args = Args::parse();

    let raw = fs::read_to_string(&args.config)
        .with_context(|| format!("kann {} nicht lesen", args.config.display()))?;
    let config: MkdocsConfig = serde_yaml::from_str(&raw)
        .with_context(|| format!("kann {} nicht als mkdocs-Config parsen", args.config.display()))?;

    if !args.docs.is_dir() {
        bail!("docs-Verzeichnis {} existiert nicht", args.docs.display());
    }

    let nodes = config
        .nav
        .iter()
        .map(parse_nav_item)
        .collect::<Result<Vec<_>>>()
        .context("kann nav in mkdocs.yml nicht parsen")?;

    let src_dir = args.output.join("src");
    fs::create_dir_all(&src_dir)?;
    copy_dir_recursive(&args.docs, &src_dir)
        .context("kann docs-Verzeichnis nicht nach src/ kopieren")?;

    let mut summary = String::from("# Summary\n\n");
    let mut missing = Vec::new();
    for node in &nodes {
        write_nav_node(node, 0, &args.docs, &mut summary, &mut missing);
    }
    fs::write(src_dir.join("SUMMARY.md"), &summary)?;

    let title = config.site_name.unwrap_or_else(|| "Book".to_string());
    let language = config.theme.language.unwrap_or_else(|| "en".to_string());
    let mut book_toml = format!(
        "[book]\ntitle = \"{}\"\nlanguage = \"{}\"\nsrc = \"src\"\n",
        title.replace('"', r#"\""#),
        language.replace('"', r#"\""#)
    );
    if let Some(desc) = &config.site_description {
        book_toml.push_str(&format!("description = \"{}\"\n", desc.replace('"', r#"\""#)));
    }
    fs::write(args.output.join("book.toml"), book_toml)?;

    let chapter_count = summary.lines().filter(|l| l.trim_start().starts_with("- [")).count();
    println!("mdBook-Projekt erzeugt in {}", args.output.display());
    println!("  {} Kapitel-Einträge (inkl. Sektionen) in src/SUMMARY.md", chapter_count);

    if !missing.is_empty() {
        println!("\nWarnung: {} nav-Einträge verweisen auf fehlende Dateien:", missing.len());
        for path in &missing {
            println!("  - {path}");
        }
    }

    let findings = scan_incompatible_syntax(&src_dir)?;
    if !findings.is_empty() {
        let total: usize = findings.values().map(|v| v.len()).sum();
        println!(
            "\nHinweis: {} Stellen in {} Dateien nutzen mkdocs/Material-Syntax ohne mdBook-Entsprechung:",
            total,
            findings.len()
        );
        for (file, hits) in &findings {
            println!("  {file}");
            for (line, reason) in hits {
                println!("    Zeile {line}: {reason}");
            }
        }
    }

    println!("\nNächste Schritte:");
    println!("  cargo install mdbook");
    println!("  cd {} && mdbook serve", args.output.display());

    Ok(())
}
