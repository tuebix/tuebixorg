---
layout: talk
title:
permalink: /programm/baur_graesing-x2go/
weight: 
menu:
---
## x2go

### <img height = "32" src="../../images/workshop.svg"> 12:00 bis 14:00 in Raum W2 

### Stefan Baur, Heinz Graesing

Der Workshop wird sich wie folgt gliedern:

#### Was ist X2Go?

- Was kann X2Go?
- Was kann X2Go NICHT?
- Wer steckt hinter X2Go?

#### Woraus besteht X2Go?

- Ein Blick in die Pakete
- Abhängigkeiten
- Dienste
- Initiales Debugging

#### Welche Probleme erzeugt ein Remote Desktop?

- Umleitung Bildschirm (1,2,...;Auflösung,...)
- Umleitung Eingabegeräte
- Umleitung Datenträger
- Umleitung Drucker
- Umleitung "Warum nicht einfach ALLES"?

#### Welche Probleme erzeugt die Remote Desktop Wiedergabe?

- Darstellung
- Protokoll- / Datenübertragung
- Benutzerrechte
- Systemressourcen
- Codeverfügbarkeit
- Ideologie

#### Erste Installation X2Goserver

- X2GoSessionsDB (sqlite)
- X2Golistsessions
- X2Goruncommand
- Welche Rechte benötigt der Benutzer?

#### Erste Installation X2GoClient

- Wahl des Desktops
- Wahl einer beliebigen Anwendung
- Anhalten und Fortführen von Sitzungen
  - Einschränkungen
- "Automatische Anmeldung"

#### Konfiguration X2GoClient

- Display
  - Packalgorithmen und Bildformate
  - Vollbild vs. Fenstermodus
- Eingabe
  - Tastaturlayouts (Debugging)
- Sound
  - Architekturen
  - Debugging
- Drucker- & Dateifreigabe
  - SSHFS
  - FUSE

#### Erweiterte X2GoServer Installation

- Absicherung des Servers
- Auswahl an freigegebenen Programmen
- X2GoSessionsDB (postgres)
- Mehrfachanmeldungen erlauben / Verhindern
- Sessions aufräumen / IDLE-Time beschränken
- Multiserver Konzepte

#### Erweiterte X2GoClient Installation

- Portable Mode
- Hidden Mode (Desktop Symbol)
- X2GoClient Commandline Optionen
  - Vorauswahl Sitzungen
  - Individualisierung
  - Client vor Veränderungen schützen
  - LDAP / Displaymanager Modus

#### Falls genug Zeit bleibt:

- Installation einer Thin Client Umgebung
- Gedanken und Techniken einer MultiNODE Installation
  - Load Balancing
  - SSH-Proxying
  - Protokollerweiterung (HTML5 Client,...)

### Vorbereitung

Für bis zu 14 Teilnehmern stehen Debian LXC Container zur Verfügung.
Sollten mehr teilnehmen wollen, sollte eine Virtuelle Maschine/Container
auf dem lokalen Rechner zur Verfügung stehen. Das Schulungsimage stellen
wir zur Verfügung.

Auf dem Client wird SSH und eine X2Goclient Installation benötigt.
Linux auf dem Client ist sehr empfehlenswert!

### Links

- <a href="http://wiki.x2go.org" target="_blank">wiki.x2go.org</a>
- <a href="http://de.wikipedia.org/wiki/X2Go" target="_blank">de.wikipedia.org/wiki/X2Go</a>
