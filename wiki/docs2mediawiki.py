#!/usr/bin/env python3
"""Erzeugt einen MediaWiki-XML-Dump (importDump.php-kompatibel) aus allen
Markdown-Artikeln unter docs/. Konvertiert Markdown -> MediaWiki-Wikitext
(Best-Effort: Überschriften, Tabellen, Code, Links, Fett/Kursiv, Listen,
Admonitions, HR)."""
import os
import re
import sys
import hashlib
import datetime
from xml.sax.saxutils import escape

DOCS = "/home/thorsten/dokument/docs"
OUT = "/home/thorsten/dokument/wiki/thorsten.xml"
TS = "2026-08-29T12:00:00Z"

# ---------------------------------------------------------------- Titel-Mapping
def path_to_title(relpath):
    """docs-relativer Pfad ohne .md  ->  Wiki-Titel (Unterseiten via /)."""
    p = relpath[:-3] if relpath.endswith(".md") else relpath
    parts = p.split("/")
    # erste Komponente großschreiben (MediaWiki $wgCapitalLinks)
    if parts:
        parts[0] = parts[0][:1].upper() + parts[0][1:]
    return "/".join(parts)

FILES = []
for root, _, names in os.walk(DOCS):
    for n in sorted(names):
        if n.endswith(".md"):
            full = os.path.join(root, n)
            rel = os.path.relpath(full, DOCS)
            FILES.append((full, rel))
FILES.sort(key=lambda t: t[1])

TITLE_BY_REL = {rel: path_to_title(rel) for _, rel in FILES}

# ---------------------------------------------------------------- Link-Auflösung
def resolve_link(cur_rel, target):
    """target aus [text](target) -> Wiki-Linkziel oder None (extern/asset)."""
    t = target.strip()
    if t.startswith(("http://", "https://", "mailto:", "//")):
        return None  # extern
    anchor = ""
    if "#" in t:
        t, anchor = t.split("#", 1)
    if t == "":
        # reiner Anker auf dieselbe Seite
        return "#" + anchor if anchor else None
    if not t.endswith(".md"):
        return None  # Bild / sonstiges Asset
    cur_dir = os.path.dirname(cur_rel)
    joined = os.path.normpath(os.path.join(cur_dir, t))
    if joined in TITLE_BY_REL:
        title = TITLE_BY_REL[joined]
        return title + ("#" + anchor if anchor else "")
    return None

# ---------------------------------------------------------------- Inline-Konvert
def conv_inline(text, cur_rel):
    # Bilder zuerst:  ![alt](src)
    def img(m):
        alt = m.group(1).strip()
        return f"''{alt}''" if alt else ""
    text = re.sub(r"!\[([^\]]*)\]\([^)]*\)", img, text)

    # Links  [text](target)
    def link(m):
        label = m.group(1).strip()
        tgt = m.group(2).strip()
        if tgt.startswith(("http://", "https://")):
            return f"[{tgt} {label}]"
        wl = resolve_link(cur_rel, tgt)
        if wl is None:
            return label
        if wl.startswith("#"):
            return f"[[{wl}|{label}]]"
        return f"[[{wl}|{label}]]"
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)

    # Inline-Code
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    # Fett
    text = re.sub(r"\*\*([^*]+)\*\*", r"'''\1'''", text)
    text = re.sub(r"__([^_]+)__", r"'''\1'''", text)
    # Kursiv (einfach)
    text = re.sub(r"(?<![\*\w])\*([^*\n]+)\*(?!\*)", r"''\1''", text)
    return text

# ---------------------------------------------------------------- Block-Konvert
ADMON_RE = re.compile(r'^(!!!|\?\?\?)\+?\s+([a-zA-Z0-9_-]+)(?:\s+"([^"]*)")?\s*$')
TABLE_SEP_RE = re.compile(r'^\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)+\|?\s*$')

def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in s.split("|")]

def convert(md, cur_rel):
    # YAML-Frontmatter entfernen
    if md.startswith("---\n"):
        end = md.find("\n---\n", 4)
        if end != -1:
            md = md[end + 5:]
    # HTML-Kommentare
    md = re.sub(r"<!--.*?-->", "", md, flags=re.S)

    lines = md.split("\n")
    out = []
    i = 0
    n = len(lines)
    in_code = False
    code_close = ""
    fence_len = 0
    fence_ch = "`"
    while i < n:
        line = lines[i]

        # Code-Fence
        mfence = re.match(r'^\s*(`{3,}|~{3,})\s*([A-Za-z0-9_+#.-]*)\s*$', line)
        if mfence and not in_code:
            fence = mfence.group(1)
            fence_len = len(fence)
            fence_ch = fence[0]
            lang = (mfence.group(2) or "").strip().lower()
            # Mermaid-Diagramme komplett auslassen (keine Mermaid-Extension)
            if lang == "mermaid":
                i += 1
                while i < n and not re.match(
                        r'^\s*%s{%d,}\s*$' % (re.escape(fence_ch), fence_len), lines[i]):
                    i += 1
                i += 1  # schließenden Fence überspringen
                out.append("''[Mermaid-Diagramm ausgelassen]''")
                continue
            in_code = True
            if lang in ("", "text", "plaintext", "console", "shell-session"):
                out.append("<pre>")
                code_close = "</pre>"
            else:
                out.append(f'<syntaxhighlight lang="{lang}">')
                code_close = "</syntaxhighlight>"
            i += 1
            continue
        if in_code:
            if re.match(r'^\s*%s{%d,}\s*$' % (re.escape(fence_ch), fence_len), line):
                out.append(code_close)
                in_code = False
            else:
                out.append(line)
            i += 1
            continue

        # Admonition
        madm = ADMON_RE.match(line)
        if madm:
            atype = madm.group(2)
            atitle = (madm.group(3) or atype).strip()
            body = []
            i += 1
            while i < n and (lines[i].startswith("    ") or lines[i].strip() == ""):
                if lines[i].strip() == "":
                    body.append("")
                else:
                    body.append(lines[i][4:])
                i += 1
            # trailing leerzeilen weg
            while body and body[-1] == "":
                body.pop()
            inner = convert("\n".join(body), cur_rel).strip()
            out.append("")
            out.append('<blockquote>')
            out.append(f"'''{escape_wt(atitle)}'''")
            out.append("")
            out.append(inner)
            out.append('</blockquote>')
            out.append("")
            continue

        # Tabelle
        if "|" in line and i + 1 < n and TABLE_SEP_RE.match(lines[i + 1]):
            header = split_row(line)
            i += 2
            rows = []
            while i < n and "|" in lines[i] and lines[i].strip():
                rows.append(split_row(lines[i]))
                i += 1
            out.append('{| class="wikitable"')
            out.append("|-")
            out.append("! " + " !! ".join(conv_inline(h, cur_rel) for h in header))
            for r in rows:
                out.append("|-")
                out.append("| " + " || ".join(conv_inline(c, cur_rel) for c in r))
            out.append("|}")
            continue

        # Überschrift
        mh = re.match(r'^(#{1,6})\s+(.*?)\s*#*\s*$', line)
        if mh:
            lvl = len(mh.group(1))
            txt = conv_inline(mh.group(2), cur_rel)
            eq = "=" * lvl
            out.append(f"{eq} {txt} {eq}")
            i += 1
            continue

        # Horizontale Linie
        if re.match(r'^\s*(-{3,}|\*{3,}|_{3,})\s*$', line):
            out.append("----")
            i += 1
            continue

        # Blockquote
        if re.match(r'^\s*>\s?', line):
            bq = []
            while i < n and re.match(r'^\s*>\s?', lines[i]):
                bq.append(re.sub(r'^\s*>\s?', '', lines[i]))
                i += 1
            out.append("<blockquote>")
            out.append(conv_inline("\n".join(bq), cur_rel))
            out.append("</blockquote>")
            continue

        # Liste
        mli = re.match(r'^(\s*)([-*+]|\d+\.)\s+(.*)$', line)
        if mli:
            indent = len(mli.group(1).replace("\t", "    "))
            depth = indent // 2 + 1
            marker = "#" if re.match(r'\d+\.', mli.group(2)) else "*"
            out.append(marker * depth + " " + conv_inline(mli.group(3), cur_rel))
            i += 1
            continue

        # normaler Absatz
        out.append(conv_inline(line, cur_rel))
        i += 1

    if in_code:
        out.append(code_close)
    text = "\n".join(out)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"

def escape_wt(s):
    return s

# ---------------------------------------------------------------- XML schreiben
def main():
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    parts = []
    parts.append('<mediawiki xmlns="http://www.mediawiki.org/xml/export-0.11/" '
                 'xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" '
                 'xsi:schemaLocation="http://www.mediawiki.org/xml/export-0.11/ '
                 'http://www.mediawiki.org/xml/export-0.11.xsd" '
                 'version="0.11" xml:lang="de">')
    parts.append("  <siteinfo>")
    parts.append("    <sitename>Thorsten Wiki</sitename>")
    parts.append("    <dbname>thorstenwiki</dbname>")
    parts.append("    <base>https://thorsten.wiki/wiki/Hauptseite</base>")
    parts.append("    <generator>docs2mediawiki (Wissen Ahrensburg)</generator>")
    parts.append("    <case>first-letter</case>")
    parts.append("    <namespaces>")
    parts.append('      <namespace key="0" case="first-letter" />')
    parts.append("    </namespaces>")
    parts.append("  </siteinfo>")

    pid = 0
    for full, rel in FILES:
        pid += 1
        title = TITLE_BY_REL[rel]
        with open(full, "r", encoding="utf-8") as fh:
            md = fh.read()
        ai_notice = (
            "''Hinweis: Diese Inhalte wurden mit Unterstützung von Künstlicher "
            "Intelligenz erstellt und redaktionell überprüft (Transparenzhinweis "
            "gemäß Art. 50 EU AI Act).''"
        )
        wt = ai_notice + "\n----\n" + convert(md, rel)
        wt += "\n----\n" + ai_notice + "\n"
        wt += ("\n''Importiert aus <code>docs/%s</code> "
               "(Wissen Ahrensburg).''\n" % rel)
        wt += "\n[[Kategorie:Wissen Ahrensburg]]\n"
        sha1 = hashlib.sha1(wt.encode("utf-8")).hexdigest()
        b = len(wt.encode("utf-8"))
        parts.append("  <page>")
        parts.append("    <title>%s</title>" % escape(title))
        parts.append("    <ns>0</ns>")
        parts.append("    <id>%d</id>" % pid)
        parts.append("    <revision>")
        parts.append("      <id>%d</id>" % pid)
        parts.append("      <timestamp>%s</timestamp>" % TS)
        parts.append("      <contributor>")
        parts.append("        <username>DocsImport</username>")
        parts.append("        <id>1</id>")
        parts.append("      </contributor>")
        parts.append("      <comment>Import aus docs/%s</comment>" % escape(rel))
        parts.append("      <model>wikitext</model>")
        parts.append("      <format>text/x-wiki</format>")
        parts.append('      <text xml:space="preserve" bytes="%d">%s</text>'
                     % (b, escape(wt)))
        parts.append("      <sha1>%s</sha1>" % sha1)
        parts.append("    </revision>")
        parts.append("  </page>")

    parts.append("</mediawiki>")
    with open(OUT, "w", encoding="utf-8") as fh:
        fh.write("\n".join(parts) + "\n")
    print("Seiten: %d" % pid)
    print("Datei : %s (%.2f MB)" % (OUT, os.path.getsize(OUT) / 1024 / 1024))

if __name__ == "__main__":
    main()
