---
layout: talk
title:
url: /2025/programm/127-bootserver2go-der-x2go-openbox-microdesktop/
weight:
menu:
---
## Bootserver2Go & der X2Go-OpenBox-MicroDesktop

### <img height = "32" src="../../../images/talk.svg"> 10:00 bis 10:50 in Raum V3 (A301)

### Stefan Baur

#### Abstract

[X2Go](https://wiki.x2go.org) ist eine freie Remote-Desktop- und Remote-Application-Software. Zu ihr gehört ein herstellerübergreifend nutzbares ThinClient-Image - in verschiedenen Ausprägungen - welches sich auch über das Netzwerk booten lässt. Mit diesem Image kann man sowohl zu X2Go- wie auch zu XDMCP- und RDP-Servern Verbindungen aufbauen.  
Mit dem Bootserver2Go kann man diese ThinClient-Images in einem bestehenden Netzwerk bereitstellen - obwohl dort bereits ein DHCP-Server (z.B. eine FritzBox oder ein Speedport-Router) läuft.

#### Beschreibung

Häufig lässt sich eine Netzboot-Möglichkeit nicht ohne größeren Eingriff in die vorhandene Umgebung testen. Sei es, weil der verwendete Router dies gar nicht unterstützt, oder weil man in der Firma nicht so einfach am DHCP-Server Änderungen vornehmen darf.

Unser Bootserver2Go integriert sich in bestehende Netzwerke, und erkennt, ob dort ein DHCP-Server mit Netzboot-Konfiguration aktiv ist. Wenn ja, stellt er sich tot, wenn nein, ergänzt er die Datenpakete des bestehenden Servers um die notwendigen Einträge. Und sollte man doch auf Probleme stoßen - Stecker ziehen reicht, um den Originalzustand wiederherzustellen, man muss keine Konfigurationsänderungen zurückrollen oder Dienste neu starten.

Als Hardware nutzen wir, um dem "2Go" im Namen gerecht zu werden, einen Raspberry Pi 4 oder neuer; optional mit Display und/oder Lautsprecher für ausführlichere Statusinformationen. Dadurch ist die Lösung leicht zu transportieren.  
Für eine dauerhafte Installation kann man natürlich genausogut leistungsfähigere, Intel-kompatible Hardware verwenden.  
Und natürlich kann unser Bootserver2Go nicht nur X2Go-ThinClient-Images bereitstellen, sondern auch andere Netzboot-Images, z.B. ein minimales Rettungssystem oder ein komplettes Desktop-Linux aus dem Debian-Live-Projekt.

Dadurch wird der Bootserver2Go auch interessant, um spontan Not-Arbeitsplätze in Betrieb zu  
nehmen, z.B. mit aus Restbeständen bunt zusammengewürfelter Hardware nach einem Katastrophenfall (Brand, Überschwemmung), oder zum schnellen Wiederanlauf nach einem Ransomware-Angriff (in diesem Fall bitte vorher alle Festplatten der betroffenen Systeme abklemmen - schützt vor Reinfektion und macht den Forensikern das Leben leichter).  
Als Terminalserver (egal ob X2Go, XDMCP, oder RDP) kann entweder vor Ort noch vorhandene (saubere) Hardware genutzt werden, oder bei ausreichender Bandbreite natürlich auch ein Cloudserver.

Bei der Live-Demo werden wir unseren neuen X2Go-OpenBox-MicroDesktop als ThinClient-Image vorführen. Dieser verfügt über einen minimalen lokal laufenden Desktop mit Browsern und Terminal-Emulationen, so dass Videokonferenzen und Mainframe/Midrange-Zugriff direkt vom Client aus funktioniert. Durch den auf dem ThinClient laufenden Desktop muss man auf dem X2Go-Server keinen kompletten Desktop, sondern nur noch einzelne Anwendungen bereitstellen, wodurch er auf günstigerer Hardware laufen bzw. mehr Benutzer versorgen kann.

Alles rund um X2Go ist im X2Go-Wiki zu finden:  
https://wiki.x2go.org/doku.php

Speziell zum Einstieg gibt es diese Wiki-Seite:  
https://wiki.x2go.org/doku.php/doc:newtox2go

#### Vorwissen

Linux-Grundkenntnisse (speziell im Bereich Administration und Netzwerk) sollten zum Verständnis des Vortrags vorhanden sein. Schon mal ein Live-Linux (egal ob übers Netz oder via USB-Stick/CD-ROM/DVD) benutzt zu haben, schadet ebenfalls nicht.

### Über mich

Stefan Baur, Jahrgang 1977, ist der aktuelle Projektmanager und Lead Evangelist des Open-Source-Projekts X2Go und geschäftsführender Gesellschafter der BAUR-ITCS UG (haftungsbeschränkt), welche Support für X2Go und eine auf X2Go basierende Security-Lösung anbietet, sowie einer der Vorstände der Open Remote Computing Association - orca e.V., einem Dachverein für freie Remote-Computing-Projekte. Nebenbei bastelt er noch an seinem privaten Projekt “Grannophone” - einem Open-Source-Videotelefon für Senioren.

