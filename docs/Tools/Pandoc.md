## Pandoc Installieren

Pandoc ist ein universeller Dokumentenkonverter, der von John MacFarlane entwickelt wurde. Er kann unter anderem Markdown, HTML, LaTeX und viele andere Formate ineinander umwandeln.

### Installation unter Ubuntu

Pandoc kann unter Ubuntu mit dem folgenden Befehl installiert werden:

```bash
sudo apt-get install pandoc
```
Mardown zu mediawiki:
```bash

pandoc -f markdown -t mediawiki -o Datenschutz.wiki Datenschutz.md
```


