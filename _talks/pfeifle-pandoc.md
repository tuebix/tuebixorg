---
layout: talk
title:
permalink: /programm/pfeifle-pandoc/
weight: 
menu:
---
## Ein&nbsp;Text-Format&nbsp;schreiben&nbsp;--&nbsp;viele&nbsp;Dokumenten-Formate&nbsp;generieren

### <img height = "32" src="../../images/talk.svg"> 13:00 bis 14:00 in Raum V4

### Kurt&nbsp;Pfeifle&nbsp;(@pdfkungfoo)

### Schlagworte

Text, Markdown, reStrukturedText, ASCIIdoc, LaTeX, ConTeXt, ODT, DOCX,
HTML, EPUB, EPUB3, DocBook, RTF, Beamer, Slidy, Slideous, S3, DZSlides,
manpages, textile, texinfo, org-mode, Beamer, Reveal.js, Impress.js,...

### Inhalt

Jeder Software-Entwickler sollte sich darum kümmern, dass seine
Programme durch eine ordentliche Dokumentation abgedeckt sind. Aber viele
Programmierer erledigen das äußerst ungern. Darum ist die Erstellung von
Dokumentation häufig ein "Stiefkind" von Projekten.
Viele Software-Benutzer würden gerne etwas zur Dokumentation beitragen
und dadurch zu Committern werden -- und manche tun es schon, oft sogar im
Zusammenhang mit mehreren Projekten. Aber dann verwenden unterschiedliche
Projekt vielleicht jeweils andere Formate und Werkzeuge zum Schreiben:
OpenDocument, HTML, LaTeX, DocBook, ...
Wäre es nicht viel besser, alles in reinem Text zu schreiben? Und dann aus
diesem Text automatisiert das End-Format zu erzeugen, welches man verwenden
möchte? Oder gar alle möglichen Endformate?
Mit der einfachen Text-Auszeichnungssprache `Markdown` ist es möglich.
Zum Konvertieren in beliebige Zielformate verwendet man das Kommandozeilen-
Tool `pandoc`. Zur Automatisierung ein `Makefile`...
----
Markdown ist ein dermaßen einfaches *Textauszeichnungsformat*, dass man bei
Kenntnis von ca. 12 verschiedenen, einfachen, sehr intuitiv zu erlernenden
Formatierungs-Regeln bereits sehr anspruchsvolle Dokumente zustande bringt
-- und zwar in allen möglichen Formaten, und in sehr vielen anpaßbaren Stilen.
1. Standard-Absätze
2. Eingerückte Absätze (Zitat-Blöcke)
3. Überschriften erster, zweiter, ... sechster Ordnung
4. Nummerierte Aufzählungen (wie diese hier)
* verschachtelte Aufzählungen (wie diese hier)
* (ich bin mir nicht sicher, ob ich dies nicht besser als 14. Regel deklarieren sollte)
5. Un-nummerierte Aufzählungen
6. Code-Beispiele: `pandoc --to=html` erzeugt HTML-Ausgabe
7. *kursiv hervorgehobene* Wörter
8. **fett hervorgehobene** Wörter
9. ***fett+kursiv hervorgehobene*** Wörter
10. [Hyper-Links](http://en.wikipedia.org/wiki/Hyperlink)
11. Bilder
12. Code-Blöcke
13. Tabellen
Wer komplexere Formatierungen benötigt, kann innerhalb des Markdown-
Quellcodes auch HTML-Schnipsel verwenden. `pandoc` gibt diese beim Übersetzen
1:1 in das Zielformat weiter. *(Falls das Ziel-Format LaTeX oder PDF ist,
kann man sogar LaTeX-Schnipsel einbetten.)*
Die Konvertierung des Markdown-Quelltextes in das gewünschte Dokumenten-Format
erfolgt durch das Kommandozeilen-Tool `pandoc`. Dabei stehen eine ganze Reihe
unterschiedlicher Ziel-Formate zur Wahl: erwähnt seien hier nur Open/LibreOffice
ODT, MS Word DOCX, LaTeX, DocBook, HTML, PDF, EPUB, EPUB3, ConTeXt und MediaWiki.
Das endgültige Aussehen der Dokumente lässt sich dadurch beeinflussen, dass
man eigene CSS-Dateien, Vorlagen- oder Referenz-Dokumente einbindet. Ansonsten
erhält man schlichte Dokumente mit den jeweils vor-eingestellten Stilen. Beim
Bau eigener CSS-Stile sind einem versierten Anwender so gut wie keine Grenzen
gesetzt, bei der Erstellung eigener Vorlagen und Referenzen gibt es ebenfalls
erstaunlich viele Möglichkeiten.
Der Workshop gliedert sich in mehrere Teile:
1. Einrichten der Erstell-Umgebung: Installation der neuesten Version von
`pandoc` aus den entsprechenden Quellen
2. Kurz-Vorstellung der `Markdown`-Syntax
3. Kurz-Vorstellung von `pandoc`
4. Besprechung des verwendeten `Makefile`
5. Erstellung eigener Dokumente in mehreren Formaten aus demselben Markdown-
Quellcode
Teilnehmer erhalten Zugriff auf ein Zip-Archiv mit folgendem Inhalt:
* Die im Vortrag / Workshop verwendeten Vortrags-Präsentationen.
* Zwei (oder mehr) Papers, welche der Autor über das *Pandoc + Markdown*-Duo
geschrieben hat.
* Eine Reihe von Markdown-Dateien, die als Ausgangspunkt der Beispiel-
Dokumente dienten.
* Ein `Makefile` (funktionierend unter Mac OS X oder Linux) zum Generieren
der fertigen Beispiel-Dokumente.
* Die für die unterschiedlichen Dokumenten-Stile der Beispiele verwendeten
CSS- und Referenz-Dateien.
* Sonstige interessanten Dateien.

### Vorwissen

* Bedarf an automatisierter Erzeugung von HTML aus einfachem Text
* Bedarf an automatisierter Erzeugung von MS Word DOCX aus Text
* Bedarf an automatisierter Erzeugung von Libre/OpenOffice ODT
* Bedarf an automatisierter EPUB-Erzeugung aus einfachem Text
* Wunsch nach LaTeX-Qualität bei PDF-Dokumenten ohne LaTeX lernen zu müssen
* Wunsch nach Beamer-Folien ohne LaTeX lernen zu müssen
* Wunsch nach einer Studien- oder Diplomarbeit ohne MS-Word
* Falls man LaTeX schon "kann": Wunsch, das Gewünschte schneller schreiben
zu können
* Falls man LaTeX schon "kann": Wunsch, das Dokument leicht auch in anderen
Formaten zur Verfügung stellen zu können
* keine Angst vor der Kommandozeile
* Bereitschaft, 12 einfache Formatierungen als "Text-Markup" zu lernen

#### Vorbereitung

Weder als Vortrag noch als Workshop ist das Thema als "Mitmach"-Thema
konzipiert. Es ist vielmehr ein "Aufpass"-Thema!
Denn dabei wird's nicht viele Folien geben, sondern fast ausschließlich
Live-Vorführung.
Im Nachhinein werden die Teilnehmer über die Tübix-Seite dann ein Archiv
mit allen entsprechenden Unterlagen herunterladen können: verwendete
Beispiel-Dateien sowie ein Transkript des Vortrags, das alle gezeigten
Kommandos nochmals wiedergibt und kurz erläutert.
Als Bonus dann noch ein Makefile, mit welchem man die Dokumenten-Erzeugung
weitgehend automatisieren kann

