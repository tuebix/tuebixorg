---
layout: talk
title:
permalink: /2018/programm/holger-gantikow-do-containers-still-not-contain-what-s-new-in-container-security/
weight:
menu:
---
## Do Containers still not contain? What's new in Container Security

### <img height = "32" src="../../../images/talk.svg"> 14:00 bis 14:50 in Raum V2

### Holger Gantikow

Der Vortrag gibt einen kurzen Überblick über den aktuellen Stand der Containertechnologie und setzt den Fokus darauf, was hier mit Hinblick auf Sicherheitsaspekte zu beachten ist, bzw. was sich zur Absicherung von containerisierten Infrastrukturen einsetzen lässt.  Beim Vortrag handelt es sich um ein erweitertes Update des TUEBIX2017-Talks [0], bei dem unter anderem Werkzeuge und Technologien wie Seccomp Profiles [1], User Namespaces (Phase 1) [2], Authorization Plugins [3], aber auch SELinux, AppArmor und Image Vulnerability Scanner [4,5], sowie Docker Bench for Security [6] vorgestellt wurden.  Zusätzlich zu diesen Werkzeugen gibt es inzwischen eine Reihe von Forschungsprojekten, welche die Basiswerkzeuge funktional erweitern, beispielsweise LiCShield [7] als AppArmor-Erweiterung, SPEAKER [8], das mittels Seccomp-Filter unterschiedliche SysCalls zur Startup- und Laufphase eines Containers zulässt und somit die Anzahl der zur Verfügung stehenden SysCalls für manche Szenarien deutlich verringern kann.  Auch existieren Ansätze und Werkzeuge [9], die sich zur Erkennung von Anomalien einsetzen lassen. Sie nutzen den Vorteil, dass, bedingt durch die Natur der Container, die Überwachung direkt auf dem Host sehr detaillierte Infos über den Containerzustand liefern, ohne dass hierzu wie bei VMs zusätzliche Komponenten notwendig wären. Im Zuge des Vortrags werden diese und weitere Technologien kurz vorgestellt und es wird betrachtet, was zu beachten ist, um Container in eine verteilte Umgebung mit Sicherheitsanforderungen einzubinden. Besonderes Augenmerk liegt auf dem Themenkomplex "Image Security" [10] und auf aktuellen Ansätzen die "ab Werk" verfügbare Werkzeuge sinnvoll erweitern, sowie zur Anomalieerkennung eingesetzt werden können.

### Vorwissen

Ein spezielles Vorwissen der Zuhörer wird nicht vorausgesetzt. Interesse an Virtualisierung, Containern und der gegebenen Problemstellung ist sicherlich von Vorteil, um eine rege Diskussion und Erfahrungsaustausch zu gewährleisten ;)

### Über mich

Holger Gantikow hat an der Hochschule Furtwangen Informatik studiert und ist bei Atos (ehemals science + computing ag) in Tübingen als Senior Systems Engineer tätig. Dort beschäftigt er sich mit der Komplexität heterogener Systeme im CAE-Berechnungsumfeld und betreut Kunden aus dem technisch-wissenschaftlichen Bereich.

