# Tools & Hilfswerkzeuge: Übersicht

Eine zentralisierte Übersicht über spezialisierte Werkzeuge, Bibliotheken und Anwendungen zur Unterstützung von Entwicklung, Datenerfassung, Analyse und Systemverwaltung. Diese Dokumentation konzentriert sich auf **Open-Source-Software**, die lokal installiert und selbst gehostet werden kann.

---

## 🛠️ Tool-Kategorien

Die Tools sind nach ihren Hauptanwendungsbereichen organisiert:

---

## 📝 Dokumentenverarbeitung & Konvertierung

Tools zur Umwandlung, Bearbeitung und Verwaltung von Dokumenten in verschiedenen Formaten.

### [Pandoc](Pandoc.md)
**Universeller Dokumentenkonverter** – Wandelt Formate ineinander um, darunter:

* **Eingabeformate**: Markdown, HTML, LaTeX, DOCX, ODT, EPUB, Jupyter Notebooks
* **Ausgabeformate**: MediaWiki, HTML, PDF, DOCX, LaTeX, EPUB, Markdown
* **Hauptfunktionen**:
  - Formatkonvertierung mit einem Befehl
  - Unterstützung für komplexe Dokumente (Tabellen, Bilder, Fußnoten)
  - Template-System für individuelle Anpassungen
  - Integration in Build-Pipelines

**Typische Anwendungsfälle:**
```bash
# Markdown zu MediaWiki
pandoc -f markdown -t mediawiki -o output.wiki input.md

# HTML zu PDF (mit LaTeX)
pandoc -f html -t pdf -o output.pdf input.html

# DOCX zu Markdown
pandoc -f docx -t markdown -o output.md input.docx
```

### Weitere Tools für Dokumentenverarbeitung

| Tool | Beschreibung | Link |
|------|--------------|------|
| **Quarto** | Wissenschaftliches Publizieren (R Markdown Alternative) | [quarto.org](https://quarto.org) |
| **AsciiDoc** | Text-basiertes Dokumentenformat | [asciidoc.org](https://asciidoc.org) |
| **Docusaurus** | Dokumentations-Generator für Web | [docusaurus.io](https://docusaurus.io) |
| **Sphinx** | Python-Dokumentationsgenerator | [sphinx-doc.org](https://www.sphinx-doc.org) |

---

## 🔍 Code-Analyse & Sicherheit

Tools zur Analyse von Code-Qualität, Abhängigkeiten und Sicherheitslücken.

### [Analysetools](Analysetool.md)
**Abhängigkeits- und Sicherheitsanalyse** für Open-Source-Projekte.

#### Abhängigkeitsanalyse

- **[deps.dev](https://deps.dev)** – Analyse von Abhängigkeiten und Versionen
- **[Snyk](https://snyk.io/)** – Schwachstellenscanner für npm, pip, Maven, etc.
- **[OSV Scanner](https://osv.dev/)** – Open-Source Vulnerability Database Scanner

**Installation & Nutzung:**
```bash
# Snyk (Node.js)
npm install -g snyk
snyk auth
snyk code test
snyk code test /pfad/zum/code

# OSV Scanner (Go)
go install github.com/google/osv-scanner/v2/cmd/osv-scanner@v2
osv-scanner -r path/to/your/project
```

### Weitere Analyse-Tools

| Tool | Zweck | Sprache |
|------|-------|---------|
| **SonarQube** | Code-Qualität & Security Analysis | Java |
| **CodeClimate** | Automatisierte Code-Reviews | Cloud/SaaS |
| **Semgrep** | Statische Code-Analyse | CLI |
| **Bandit** | Python Security Linter | Python |
| **ESLint** | JavaScript/TypeScript Linter | Node.js |
| **Pylint** | Python Code-Analyse | Python |

---

## ⚡ Performance & Benchmarking

Tools zur Leistungsmessung und Optimierung von Anwendungen und Frameworks.

### [Web Frameworks Benchmark](Benchmark.md)
**Leistungsvergleich von Web-Frameworks** – Messung und Visualisierung der Performance.

#### Benchmark-Plattformen

- **[TechEmpower Benchmarks](https://www.techempower.com/benchmarks/)** – Standard für Web-Framework-Vergleiche
  - Testet Hundert Frameworks
  - Verschiedene Szenarien (JSON, Datenbank, Plaintext)
  - Regelmäßige Updates

- **[Web Frameworks Benchmark Visualizer](https://web-frameworks-benchmark.netlify.app/)** – Visuelle Darstellung der TechEmpower-Daten

**Kategorien:**
- **JSON-Serialisierung** – API-Performance
- **Datenbankzugriff** – ORM & Query-Performance
- **Server-zu-Server** – HTTP/2, WebSockets
- **Plaintext** – Rohdaten-Throughput

### Weitere Performance-Tools

| Tool | Zweck | Link |
|------|-------|------|
| **Apache JMeter** | Last- und Leistungstests | [jmeter.apache.org](https://jmeter.apache.org) |
| **k6** | Modernes Load-Testing | [k6.io](https://k6.io) |
| **Locust** | Python-basiertes Load-Testing | [locust.io](https://locust.io) |
| **Wrk** | HTTP-Benchmarking | [github.com/wg/wrk](https://github.com/wg/wrk) |
| **AB (Apache Bench)** | Einfaches Benchmarking | [httpd.apache.org](https://httpd.apache.org) |

---

## 🐳 Containerisierung & Deployment

Tools für Container, Orchestrierung und Deployment.

| Tool | Beschreibung | Link |
|------|--------------|------|
| **Docker** | Container-Plattform | [docker.com](https://www.docker.com) |
| **Podman** | Docker-Alternative (daemonless) | [podman.io](https://podman.io) |
| **Docker Compose** | Multi-Container-Anwendungen | [docs.docker.com](https://docs.docker.com/compose) |
| **Kubernetes** | Container-Orchestrierung | [kubernetes.io](https://kubernetes.io) |
| **Helm** | Kubernetes Package Manager | [helm.sh](https://helm.sh) |
| **Lens** | Kubernetes IDE | [k8slens.dev](https://k8slens.dev) |

---

## 📊 Monitoring & Logging

Tools zur Überwachung von Systemen, Anwendungen und Infrastruktur.

| Tool | Beschreibung | Link |
|------|--------------|------|
| **Prometheus** | Metriken-Sammlung & Alerting | [prometheus.io](https://prometheus.io) |
| **Grafana** | Visualisierung & Dashboards | [grafana.com](https://grafana.com) |
| **ELK Stack** | Log-Management (Elasticsearch, Logstash, Kibana) | [elastic.co](https://www.elastic.co) |
| **Loki** | Log-Aggregation (von Grafana) | [grafana.com/loki](https://grafana.com/loki) |
| **Sentry** | Error-Tracking | [sentry.io](https://sentry.io) |
| **New Relic** | Application Performance Monitoring | [newrelic.com](https://newrelic.com) |

---

## 🔧 Versionskontrolle & CI/CD

Tools für Code-Management und automatisierte Workflows.

| Tool | Beschreibung | Link |
|------|--------------|------|
| **Git** | Versionskontrollsystem | [git-scm.com](https://git-scm.com) |
| **GitHub CLI** | GitHub-Befehlszeile | [cli.github.com](https://cli.github.com) |
| **GitLab CLI** | GitLab-Befehlszeile | [docs.gitlab.com](https://docs.gitlab.com/ee/user/project/cli) |
| **GitHub Actions** | CI/CD für GitHub | [github.com/features/actions](https://github.com/features/actions) |
| **GitLab CI/CD** | CI/CD für GitLab | [docs.gitlab.com](https://docs.gitlab.com/ee/ci) |
| **Jenkins** | Automatisierungsserver | [jenkins.io](https://www.jenkins.io) |
| **Drone** | Container-native CI/CD | [drone.io](https://www.drone.io) |

---

## 🗄️ Datenbanken & Datenmanagement

Tools für Datenbankverwaltung, Migration und Analyse.

| Tool | Beschreibung | Link |
|------|--------------|------|
| **pgAdmin** | PostgreSQL-Verwaltung | [pgadmin.org](https://www.pgadmin.org) |
| **DBeaver** | Universeller Datenbank-Client | [dbeaver.io](https://dbeaver.io) |
| **TablePlus** | Moderner GUI-Client | [tableplus.com](https://tableplus.com) |
| **MySQL Workbench** | MySQL-Verwaltung | [mysql.com](https://www.mysql.com/products/workbench) |
| **Redis CLI** | Redis-Befehlszeile | [redis.io](https://redis.io) |
| **MongoDB Compass** | MongoDB GUI | [mongodb.com](https://www.mongodb.com/products/compass) |

---

## 🌐 Netzwerk & Sicherheit

Tools für Netzwerkanalyse, Sicherheitstests und Proxy-Management.

| Tool | Beschreibung | Link |
|------|--------------|------|
| **Nginx** | Webserver & Reverse Proxy | [nginx.org](https://nginx.org) |
| **Apache** | Webserver | [apache.org](https://httpd.apache.org) |
| **Caddy** | Automatischer HTTPS-Webserver | [caddyserver.com](https://caddyserver.com) |
| **Traefik** | Cloud-native Reverse Proxy | [traefik.io](https://traefik.io) |
| **Wireshark** | Netzwerk-Protokoll-Analyse | [wireshark.org](https://www.wireshark.org) |
| **Nmap** | Netzwerk-Scanning | [nmap.org](https://nmap.org) |
| **OpenSSL** | SSL/TLS-Tools | [openssl.org](https://www.openssl.org) |

---

## 💻 Entwicklungsumgebung

Tools für lokale Entwicklung, Debugging und Testing.

| Tool | Beschreibung | Link |
|------|--------------|------|
| **Visual Studio Code** | Code-Editor | [code.visualstudio.com](https://code.visualstudio.com) |
| **IntelliJ IDEA** | Java/Kotlin IDE | [jetbrains.com/idea](https://www.jetbrains.com/idea) |
| **PyCharm** | Python IDE | [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm) |
| **WebStorm** | JavaScript/TypeScript IDE | [jetbrains.com/webstorm](https://www.jetbrains.com/webstorm) |
| **VS Code Extensions** | Plugins für VS Code | [marketplace.visualstudio.com](https://marketplace.visualstudio.com) |

---

## 🧪 Testing

Tools für automatisiertes Testen von Software.

| Tool | Beschreibung | Link |
|------|--------------|------|
| **JUnit** | Unit-Testing für Java | [junit.org](https://junit.org) |
| **pytest** | Testing Framework für Python | [pytest.org](https://docs.pytest.org) |
| **Jest** | JavaScript Testing | [jestjs.io](https://jestjs.io) |
| **Mocha** | JavaScript Test Framework | [mochajs.org](https://mochajs.org) |
| **Cypress** | End-to-End Testing | [cypress.io](https://www.cypress.io) |
| **Playwright** | Browser-Automatisierung | [playwright.dev](https://playwright.dev) |
| **Selenium** | Web-Automatisierung | [selenium.dev](https://www.selenium.dev) |
| **Postman** | API-Testing | [postman.com](https://www.postman.com) |

---

## 📦 Paketmanagement

Tools für Paket- und Abhängigkeitsmanagement.

| Tool | Sprache | Link |
|------|---------|------|
| **npm** | JavaScript | [npmjs.com](https://www.npmjs.com) |
| **Yarn** | JavaScript | [yarnpkg.com](https://yarnpkg.com) |
| **pnpm** | JavaScript | [pnpm.io](https://pnpm.io) |
| **pip** | Python | [pypi.org](https://pypi.org) |
| **Poetry** | Python | [python-poetry.org](https://python-poetry.org) |
| **pipenv** | Python | [pipenv.pypa.io](https://pipenv.pypa.io) |
| **Maven** | Java | [maven.apache.org](https://maven.apache.org) |
| **Gradle** | Java/Kotlin | [gradle.org](https://gradle.org) |
| **Composer** | PHP | [getcomposer.org](https://getcomposer.org) |
| **NuGet** | .NET | [nuget.org](https://www.nuget.org) |

---

## 🚀 DevOps & Infrastruktur

Tools für Infrastructure as Code und Automatisierung.

| Tool | Beschreibung | Link |
|------|--------------|------|
| **Ansible** | Konfigurationsmanagement | [ansible.com](https://www.ansible.com) |
| **Terraform** | Infrastructure as Code | [terraform.io](https://www.terraform.io) |
| **Pulumi** | Infrastructure as Code (Code-First) | [pulumi.com](https://www.pulumi.com) |
| **Vagrant** | Entwicklungsumgebungen | [vagrantup.com](https://www.vagrantup.com) |
| **Packer** | Image-Building | [packer.io](https://www.packer.io) |
| **Consul** | Service Discovery | [consul.io](https://www.consul.io) |
| **Vault** | Secrets Management | [vaultproject.io](https://www.vaultproject.io) |

---

## 🔄 Backup & Recovery

Tools für Datensicherung und Wiederherstellung.

| Tool | Beschreibung | Link |
|------|--------------|------|
| **BorgBackup** | Dedup-Backup | [borgbackup.org](https://www.borgbackup.org) |
| **Restic** | Sichere Backups | [restic.net](https://restic.net) |
| **Duplicati** | GUI-Backup | [duplicati.com](https://www.duplicati.com) |
| **rsync** | Datei-Synchronisation | [rsync.samba.org](https://rsync.samba.org) |
| **Bareos** | Backup-Suite | [bareos.com](https://www.bareos.com) |

---

## 📱 Mobile Entwicklung

Tools für mobile App-Entwicklung.

| Tool | Beschreibung | Link |
|------|--------------|------|
| **Android Studio** | Android IDE | [developer.android.com](https://developer.android.com/studio) |
| **Xcode** | iOS/macOS IDE | Apple Developer |
| **Flutter** | Cross-Platform Framework | [flutter.dev](https://flutter.dev) |
| **React Native** | Cross-Platform (JavaScript) | [reactnative.dev](https://reactnative.dev) |
| **Ionic** | Hybrid-Apps | [ionicframework.com](https://ionicframework.com) |
| **Capacitor** | Native Runtime für Web-Apps | [capacitorjs.com](https://capacitorjs.com) |

---

## 🎨 Design & UI/UX

Tools für Design, Prototyping und UI-Entwicklung.

| Tool | Beschreibung | Link |
|------|--------------|------|
| **Figma** | UI/UX Design | [figma.com](https://www.figma.com) |
| **Inkscape** | Vektor-Grafik | [inkscape.org](https://inkscape.org) |
| **GIMP** | Bildbearbeitung | [gimp.org](https://www.gimp.org) |
| **Blender** | 3D-Modellierung | [blender.org](https://www.blender.org) |
| **Tailwind CSS** | Utility-First CSS | [tailwindcss.com](https://tailwindcss.com) |
| **Bootstrap** | CSS-Framework | [getbootstrap.com](https://getbootstrap.com) |

---

## 📚 Dokumentation & Wissensmanagement

| Tool | Beschreibung | Link |
|------|--------------|------|
| **MkDocs** | Markdown-basierte Docs | [mkdocs.org](https://www.mkdocs.org) |
| **Docusaurus** | Facebook Docs-Generator | [docusaurus.io](https://docusaurus.io) |
| **Sphinx** | Python-Docs | [sphinx-doc.org](https://www.sphinx-doc.org) |
| **GitBook** | Kollaborative Docs | [gitbook.com](https://www.gitbook.com) |
| **Obsidian** | Wissensdatenbank | [obsidian.md](https://obsidian.md) |
| **Notion** | All-in-One Workspace | [notion.so](https://www.notion.so) |

---

## 🎯 Empfohlene Tool-Kombinationen

### Web-Entwicklung
- **Frontend**: VS Code + ESLint + Prettier + Jest
- **Backend**: Docker + Node.js/Python + PostgreSQL
- **Deployment**: GitHub Actions + Docker Compose + Nginx
- **Monitoring**: Prometheus + Grafana + Loki

### Datenanalyse
- **Python**: JupyterLab + Pandas + NumPy + Matplotlib
- **R**: RStudio + tidyverse + ggplot2
- **Datenbank**: PostgreSQL + DBeaver + pgAdmin
- **Visualisierung**: Grafana + Metabase

### Mobile Entwicklung
- **Android**: Android Studio + Kotlin + Jetpack Compose
- **iOS**: Xcode + Swift + SwiftUI
- **Cross-Platform**: VS Code + Flutter/Dart
- **Backend**: Firebase + Node.js

---

## 🔗 Verwandte Dokumentationsbereiche

* [Server-Konfiguration](../Server/Software.md) – Server-Tools und -Einstellungen
* [IDE & Entwicklungsumgebung](../IDE/index.md) – Entwicklungs-Tools
* [Datenerfassung](../Datenerfassung/index.md) – Datenerfassungstools
* [Dokument Erstellen](../Dokument_Erstellen/index.md) – Dokumentations-Tools

---

## 📖 Weiterführende Ressourcen

### Tool-Vergleiche
- [Static Site Generators](https://www.staticgen.com/) – Vergleich von SSG-Tools
- [CI/CD Tools Comparison](https://about.gitlab.com/devops-tools/) – CI/CD-Tools im Vergleich
- [Container Orchestration](https://www.cncf.io/) – CNCF Landscape

### Tutorials & Guides
- [DevOps Roadmap](https://roadmap.sh/devops) – Lernpfad für DevOps
- [Full Stack Development Roadmap](https://roadmap.sh/full-stack) – Full Stack Lernpfad
- [Testing Strategies](https://martinfowler.com/articles/practical-test-pyramid.html) – Test-Pyramide

### Communities
- [DevOps Chat](https://devops.chat/) – DevOps Community
- [r/devops](https://www.reddit.com/r/devops/) – DevOps Subreddit
- [Stack Overflow](https://stackoverflow.com/) – Q&A für Entwickler
