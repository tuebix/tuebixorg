---
layout: talk
title:
url: /2025/programm/145-praktische-einfhrung-in-nixos/
weight:
menu:
---
## Praktische Einführung in NixOS

### <img height = "32" src="../../../images/workshop.svg"> 14:00 bis 15:50 in Raum W3 (C111)

### Yann Büchau

#### Abstract

NixOS durch Praxisbeispiele kennenlernen

#### Beschreibung

NixOS ist eine fast 20 Jahre bestehende Linux-Distribution mit dem radikal anderen Ansatz, sämtliche Software und Einstellungen des Betriebssystems reproduzierbar in Konfigurationsdateien zu deklarieren. Dazu wird die `nix`-Sprache verwendet, mit der beliebige Software reproduzierbar gebaut werden kann. Das ermöglicht Dinge wie:

- Updates, die durch Unterbrechnung nicht kaputt gehen können  
- Zusammenstellung beliebiger Versionen von Programmen  
- einfaches Konfigurieren auch komplizierter Dienste (z.B. `services.nextcloud.enable = true;`)
- Testen von Änderungen in VMs (`nixos-rebuild build-vm`)
- unabhängige Entwicklungsumgebungen für Projekte (`nix-shell -p python git ...`)
- einfaches Bauen für andere Architekturen (z.B. fertige SD-Karten-Abbilder für Raspberry Pi)
- und noch viel mehr. 

In diesem Workshop schauen wir uns das in der Praxis an.

#### Vorwissen

Laptop mitbringen, möglichst schon versuchen, nix vorher zu installieren (https://nixos.org/download/, oben unter "Nix". Geht auf allen Linux-Distributionen und stört das restliche Betriebssystem nicht. Oder man macht sich eine NixOS VM, geht natürlich auch.).

Ansonsten die grundlegenden Linux Dinge, Textdateien bearbeiten, im Terminal arbeiten, bisschen git, etc. sollte beherrscht werden.

