---
layout: talk
title:
url: /2026/programm/202-resilient-raspberry-pi-os-der-unkaputtbare-raspi/
weight:
menu:
---
## Resilient Raspberry Pi OS - der "unkaputtbare" Raspi

### <img height = "32" src="../../../images/talk.svg"> 10:00 bis 10:50 in Raum V4 (C118a)

### Stefan Baur

#### Abstract

Hier geht es um diverse Hard- und Software-Tricks, wie man ein Raspberry Pi OS so installiert, dass es nahezu "unkaputtbar" ist. Dazu gibt es fertige Installationsskripte für Beispielanwendungen. Einige der Tricks sind gar nicht so neu - aber gefühlt vor über 20 Jahren wieder in Vergessenheit geraten.

#### Beschreibung

Wir beginnen mit der Auswahl eines geeigneten Speichermediums (Spoiler: keine MicroSD-Karten), hangeln uns durch den offiziellen Installer der Raspberry Pi Foundation, und biegen dann mit unserem Installationsskript noch vor dem ersten Start das erstellte Image nach unseren Vorstellungen um. Dabei nutzen wir Konzepte, die zum Teil noch aus alten, zu OS/2-Zeiten von IBM verfassten Redbooks stammen, aber auch heute auf dem Raspberry Pi noch (oder wieder) von Nutzen sind.

Am Schluss hat man dann zum Beispiel einen kleinen Port-9100-Printserver, mit dem man seinen billigen USB-only-Drucker plötzlich netzwerkfähig machen kann, oder ein Mailcow-Demo-Setup (sogar mit Docker),  oder die Entwicklungsbasis für [Grannophone](https://www.grannophone.de)-Images, oder einen [X2Go](https://wiki.x2go.org)-Server oder -ThinClient, oder einen WLAN-Accesspoint (oder umgekehrt, einen WLAN-zu-LAN-Adapter für Geräte, die zwingend ein LAN-Kabel als Uplink erwarten) oder einfach nur eine Minimalinstallation, bei der die Eingabe von "sl" dazu führt, dass eine Dampflok als ASCII-Animation über die Konsole huscht, und die man als Basis für eigene Erweiterungen nutzen kann.

Allen diesen Installationsvarianten ist gemein, dass sie einen ungeplanten Stromausfall zumindest soweit problemlos überleben, dass das Betriebssystem danach wieder startet und über SSH erreichbar ist (Services, die lokal Daten speichern müssen, wie z.B. Mailcow, brauchen ggf. manuelle Nacharbeit). Genauso hat man zu jedem eingespielten Update, wenn man sich an unsere Anleitung hält, immer eine automatisiert (z.B. per watchdog oder Startup-Skript) bzw. aus der Ferne auslösbare Fallback-Möglichkeit auf den vorherigen Stand.

Der finale Clou: Hat man sich sowohl Produktionsumgebung als auch Fallback zerschossen, kommt man mit einem Hardwareschalter beim nächsten Neustart in eine Rettungsumgebung.

### Über mich

Stefan Baur, Jahrgang 1977, ist der aktuelle Projektmanager und Lead Evangelist des Open-Source-Projekts X2Go und geschäftsführender Gesellschafter der [BAUR-ITCS UG (haftungsbeschränkt)](https://www.baur-itcs.de), welche Support für [X2Go](https://wiki.x2go.org) und eine auf X2Go basierende Security-Lösung anbietet, sowie einer der Vorstände der [Open Remote Computing Association - orca e.V.](https://orca-ev.de), einem Dachverein für freie Remote-Computing-Projekte. Nebenbei bastelt er noch an seinem privaten Projekt “[Grannophone](https://www.grannophone.de)” - einem Open-Source-Videotelefon für Senioren.

