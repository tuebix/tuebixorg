---
layout: talk
title:
permalink: /programm/graesing-x2go/
weight: 
menu:
---
## X2Go

### <img height = "32" src="../../images/workshop.svg"> 12:00 bis 14:00 in Raum W2

### Heinz Graesing

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
- Drucker- und Dateifreigabe
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

#### Was wird benötigt?
- Eine vom Client aus erreichbare Virtuelle Masschine
  * Debian Jessie (Basisystem, ohne SystemD)
  * alternativ: LXC Container auf der Trainer Maschine
  * LXC Container kann per USB-Stick "herumgreicht" werden
- Eine von X2GoClient unterstütztes Clientbetriebsystem
  * Trainer verwenden Debian Jessie
- Internetzugang (Uni Tübingen, Daten folgen)
- Kennnisse
- Container/Virtualiserung (als Servermaschine)
  * ssh
  * vim
  * Xorg
  * Geduld

### Links

- <a href="http://wiki.x2go.org" target="_blank">wiki.x2go.org</a>
- <a href="http://de.wikipedia.org/wiki/X2Go" target="_blank">de.wikipedia.org/wiki/X2Go</a>
