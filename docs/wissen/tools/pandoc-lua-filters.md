# Praxis-Guide: Pandoc Custom Lua-Filter

**Pandoc Lua-Filter** erlauben die direkte Manipulation des Abstract Syntax Trees (AST) von Markdown-Dokumenten beim Konvertieren zu PDF, HTML oder DOCX.

---

## 🛠️ 1. Beispiel 1: Alle externen Links im PDF rot hervorheben (`red_links.lua`)

```lua
-- red_links.lua
function Link(el)
    if el.target:match("^http") then
        return pandoc.Span(el.content, {style = "color: red;"})
    end
    return el
end
```

---

## 🛠️ 2. Beispiel 2: Verwandlung von Hinweisen in Callout-Boxen (`callouts.lua`)

```lua
-- callouts.lua
function BlockQuote(el)
    -- Prüft ob das Zitat mit [!NOTE] beginnt
    local first_block = el.content[1]
    if first_block and first_block.t == "Paragraph" then
        local first_inline = first_block.content[1]
        if first_inline and first_inline.t == "Str" and first_inline.text == "[!NOTE]" then
            table.remove(first_block.content, 1) # Entferne den Tag
            return pandoc.Div(el.content, {class = "admonition note"})
        end
    end
    return el
end
```

---

## ⚡ 3. Lua-Filter anwenden

```bash
pandoc input.md --lua-filter=red_links.lua --lua-filter=callouts.lua -o output.pdf --pdf-engine=typst
```

---

## 🔗 Verwandte Themen
* [Pandoc Export-Pipeline](pandoc-export-pipeline.md) – Export-Pipelines
* [Pandoc Übersicht](pandoc.md) – Grundlagen
* [Analysetool](analysetool.md) – Dokumentenanalyse
