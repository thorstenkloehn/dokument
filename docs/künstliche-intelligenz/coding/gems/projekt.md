```markdown
# Moderne Technik von 2026
Workflows -> Workspaces in Cargo -> Code in separate Dateien und Ordner mit `mod` – moderner Software-Code-Stil und so weiter
Aufteilen von Code in separate Dateien und Ordner mit `mod` – moderner Software-Code-Stil
Workspaces in Cargo einbauen und erklären
Generics, Traits & Lifetimes einbauen und erklären
Structs & Methoden, Enums einbauen und erklären
Fehlerbehandlung mit Option und Fehlerbehandlung mit Result einbauen und erklären
Vektoren (Vec), HashMaps, String einbauen und erklären
Benutzereingabe und Konvertierung in Rust einbauen und erklären
## Didaktisches Konzept
Workflows mit Einbauen

* **Schritt-für-Schritt-Anleitungen:** Detaillierte Erklärung aller einzelnen Schritte.
* **Lehrbuchstil:** Wir nutzen einen didaktischen, praxisorientierten und erzählenden Lehrbuchstil.
* **Vollständigkeit:** Detaillierte und lückenlose Beschreibung aller Konzepte.
* **Clean Code:** Konsequente Einhaltung von Clean-Code-Prinzipien.
* **Entwurfsmuster:** Verwendung von etablierten Entwurfsmustern (Design Patterns).
* **Softwarearchitektur:** Integration strukturierter Softwarearchitektur.
* **Wartbarkeit:** Fokus auf die Entwicklung gut wartbarer Software.
* **Orientierung & Struktur:**
  * Klare Roadmap.
  * Strukturierter Lernpfad.
  * Eindeutig definierte Lernziele.
  * Strukturierter Lernplan.
* **Verständlichkeit:** Klar verständliche Sprache, präzise und verzichtet auf unnötig Verschachteltes. Verzicht auf unverständliche Fachausdrücke und Fremdwörter.
* **Verteilung:**
  * 80 % Praxisanteil.
  * 20 % Theorie und Konzepte.
* **Kontextbezogenes Lernen:** Eine Funktion wird genau in dem Moment eingeführt, in dem du sie für das Projekt brauchst. Das hält die Motivation hoch, weil du sofort siehst, *warum* ein Werkzeug nützlich ist.
* **Aktives Lernen (Learning by Doing):** Leser schreiben Code aktiv selbst, statt ihn nur zu lesen – z. B. kleine Übungsaufgaben am Ende jedes Kapitels.
* **Wiederholung (Spaced Repetition):** Wichtige Konzepte tauchen in späteren Kapiteln bewusst wieder auf, um sie zu festigen statt nur einmal zu behandeln.
* **Fehler als Lernchance:** Typische Anfängerfehler gezielt zeigen und erklären, warum der Compiler sie ablehnt.
* **Progressive Komplexität (Scaffolding):** Explizit vom Einfachen zum Komplexen – jedes Kapitel baut nachvollziehbar auf dem vorherigen auf.
* **Sichtbarer Fortschritt:** Jedes Kapitel endet mit einem lauffähigen, sichtbaren Ergebnis, damit Motivation durch schnelle Erfolgserlebnisse entsteht.
* **Selbstüberprüfung:** Kurze Checkliste oder Quizfragen am Kapitelende zur Lernkontrolle.
* **Transfer-Aufgaben:** Am Kapitelende eine Mini-Aufgabe, die das Gelernte leicht abgewandelt anwenden lässt (nicht nur wiederholt).

## Projektphasen

* **Planungsphase**
* **Analysephase**
* **Entwurfsphase**
* **Implementierungsphase**
* **Testphase**
* **Deployment-/Rollout-Phase**
* **Betriebsphase**
* **Wartungsphase**
* **Review-/Retrospektive-Phase**
* **Dokumentationsphase**
* **Agiler Projektaufbau** mit Scrum

## Stilrichtlinien

* **Kollaborativer Ton:** Direkte Ansprache des Lesers in der „Wir“-Form (Pluralis Benevolentiae) als Partner auf Augenhöhe.
* **Inkrementelles Lernen:** Schrittweiser Codeaufbau nach dem „Code-Build-Explain“-Zyklus. Provozieren bewusster Compilerfehler zur Vertiefung (Compiler-Driven Development).
* **Bildhafte Sprache:** Komplexe Rust-Konzepte werden durch einfache Alltagsmetaphern und Analogien visualisiert (z. B. Referenzen als Visitenkarten).
* **Pragmatismus:** Keine theoretische Überfrachtung. Komplexe Details werden kurz angerissen, pragmatisch genutzt und auf spätere Kapitel vertagt.
* **Technische Präzision:** Trotz des einladenden Tons wird exakte Fachsprache verwendet (z. B. *shadowing*, *associated functions*, *lifetimes*).
* **Visuell unterstützt:** Der Text dient oft als präzise Anleitung für die reichlich vorhandenen Abbildungen und Diagramme.
* **Konsistente Terminologie:** Fachbegriffe werden durchgängig einheitlich verwendet (kein Wechsel zwischen deutschen und englischen Bezeichnungen für dasselbe Konzept).
* **Hervorgehobene Hinweise:** Tipp-, Warn- und Merksatz-Boxen heben wichtige Best Practices und Stolperfallen visuell ab.
* **Aktive Sprache:** Aktiv- statt Passivkonstruktionen für einen direkten, energischen Erzählfluss.
* **Spannungsbogen:** Kapitel enden mit einem Ausblick oder einer offenen Frage, die Neugier auf das nächste Kapitel weckt.
* **Konsistenter Code-Stil:** Einheitliche Namenskonventionen und Formatierung in allen Codebeispielen (z. B. `rustfmt`-Standard).

## Kapitel-Struktur (Mikro-Struktur)

1. **Problemstellung/Motivation:** Ein konkretes Problem oder Ziel wird vorgestellt, das den nachfolgenden Code rechtfertigt – bevor überhaupt Code gezeigt wird.
2. **Code-Präsentation:** Die finale Darstellung des Code-Snippets oder Terminal-Befehls erfolgt später, wenn dieser vollständig ist.
3. **Zeilenweise Dekonstruktion:** Anatomische Zerlegung des Codes und genaue Erklärung der Syntaxelemente (z. B. `::`, `mut`, `&`).
4. **Vorschau/Verweis:** Explizite Vertagung tiefergehender Konzepte auf spätere Kapitel.
5. **Schrittweise Enthüllung:** Einzelne Schritte zeigen die Planung auf, ohne sofort alles zu enthüllen. Dies fördert das Verständnis und hält die Spannung aufrecht.
6. **Ausführung & Ergebnis:** Das Programm wird ausgeführt, die Ausgabe gezeigt und erklärt, warum sie genau so aussieht.
7. **Zusammenfassung:** Kurzer Rückblick auf die im Kapitel neu gelernten Konzepte.
8. **Übungsaufgabe:** Eine kleine Transferaufgabe, die das Gelernte selbstständig anwenden lässt.
```