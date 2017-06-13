---
layout: talk
title:
permalink: /2017/programm/christian-brauner-lxd/
weight:
menu:
---
## LXD

### <img height = "32" src="../../../images/talk.svg"> 12:00 bis 13:00 in Raum V4

### Christian Brauner

LXD ist ein Container Management Daemon der auf der Low-Level Container Runtime
LXC aufbaut und eine REST API zum Verwalten von mehreren Container Hosts über
das Internet bereit stellt. Dieser Vortrag wird die Hauptfeatures von LXD
vorstellen, eine gründliche Live-Demo der Fähigkeiten geben und die
gegenwärtigen Features, an denen gearbeitet wird (sowohl im Kernel als auch in
LX{C,D} selbst) diskutieren.
Die Arbeit an LXD wurde vor gut anderthalb Jahren vom selben Team begonnen, die
LXC geschrieben haben. Unter den Maintainern befinden sich zum Teil dieselben
Leute, die die Features, die Container überhaupt möglich gemacht haben, im
Kernel implementiert haben. LXD baut auf der low-level Container Runtime LXC
auf und wurde von Grund auf neu durchdacht, mit einem Fokus auf Sicherheit,
Zuverlässigkeit und Geschwindigkeit. Das Ziel ist es dabei, jede existierende
Sicherheitsfunktion des Linux Kernels zu nutzen.
LXD betreibt System Containers und keine Process Containers (docker, rocket,
...), d.h. LXD kümmert sich ausschließlich um Container, die ein vollständiges
Linux Betriebssystem laufen lassen, genau wie man es von einer virtuellen
Maschine gewohnt ist.

### Über mich

LX{C,D} core dev.

### Links

- <a href="https://linuxcontainers.org/lxd/try-it" target="_blank">https://linuxcontainers.org/lxd/try-it</a>
- <a href="https://github.com/lxc/lxd" target="_blank">https://github.com/lxc/lxd</a>
- <a href="https://github.com/lxc/lxc" target="_blank">https://github.com/lxc/lxc</a>
- <a href="https://linuxcontainers.org" target="_blank">https://linuxcontainers.org</a>
