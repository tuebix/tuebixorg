---
layout: talk
title:
permalink: /2019/programm/michael-weiss-nixos-ein-ueberblick/
weight:
menu:
---
## Nix(OS) - Ein Überblick

### <img height = "32" src="../../../images/lightning.svg"> 16:25 bis 16:30 in Raum V3

### Michael Weiss

Ein kurzer Überblick über Nix(OS), Nixpkgs und weitere nützliche Tools. Es geht v.a. darum die Konzepte zu vermitteln sowie die Unterschiede zu klassischen Paket-Managern aufzuzeigen (mögliche Vor- und Nachteile).

Nix ist ein funktionaler package manager, der auch auf anderen Betriebssystem genutzt werden kann, ohne Konflikte mit dem bestehenden package manager zu bekommen. NixOS ist eine auf Nix basierende Linux-Distribution, mit der neben den Software-Paketen zusätzlich auch die System-Konfiguration über Nix verwaltet werden kann. Die Paket-Definitionen und NixOS Module zur Systemkonfiguration werden in Nixpkgs, einem großen Git Repository, zentral verwaltet.

Nix(OS) verfügt unter anderem über folgende Features:  
- Transparent source/binary model  
- Declarative (system configuration)
- Reproducible builds  
- Multi-user, multi-version (no conflicts)
- Portable (Linux, macOS, ...)
- Reliable and atomic updates  
- Rollbacks

### Vorwissen

Grobe Kenntnisse eines Paket-Managers wären evtl. hilfreich.

### Über mich

Nixpkgs package maintainer seit 2017 (ca. 50 Pakete und 4 Module), davor Gentoo user. Begeistert für FLOSS, GNU/Linux, Networking ("Internet"), reproducible builds, etc. Aktuell Informatik-Student an der Universität Tübingen.

### Links

- <a href="https://nixos.org/" target="_blank">NixOS Website</a>
- <a href="https://github.com/NixOS/nixpkgs/" target="_blank">Nixpkgs (GitHub)</a>
- <a href="https://primeos.github.io/nixos-slides/" target="_blank">Folien der vollständigen Präsentation</a>
- <a href="https://github.com/primeos" target="_blank">Mein GitHub Profil</a>