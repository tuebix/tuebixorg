---
layout: talk
title:
url: /2025/programm/151-read-linux-networking-code-without-c-ing/
weight:
menu:
---
## Read linux networking code without C-ing

### <img height = "32" src="../../../images/talk.svg"> 17:30 bis 17:50 in Raum V2 (F112)

### Moritz Flüchter

#### Abstract

Der Linux-Kernel-Quellcode wirkt auf den ersten Blick abschreckend, kompliziert und schwer zugänglich - und auf den zweiten und dritten Blick auch.  
Dabei ist es durchaus möglich Teile des Kernels zu lesen und zu verstehen wenn ein paar Grundkonzepte bekannt sind.

Ziel dieses Vortrags ist es, den Einstieg in das Lesen des Quellcodes im Bereich der Netzwerkprotokolle zu erleichtern, auch ohne tiefgehende C-Kenntnisse.  
Dazu werden zentrale Konzepte des Linux-Netzwerkstacks kurz erklärt und gezeigt, wie man diese als Orientierung nutzen kann, um sich im Code zurechtzufinden.

Ein vollständiges Verständnis des Kernels ist dabei nicht das Ziel (das wäre in 20 Minuten auch ziemlich schwer), dafür aber ein erster Schritt und Anreiz zur eigenen Erforschung des Kernels.

#### Beschreibung

Im Rahmen eines Projektes habe ich mich das erste Mal richtig mit dem Quellcode des Netzwerkstacks im Linux Kernel beschäftigt. Dabei ist einiges an Wissen zusammengekommen wie man einfacher mit dem Linux-Quellcode umgehen kann. Vor Allem, da ich selber noch nie in C programmiert habe (außer im ersten Semester, aber das zählt nicht).

Das betrifft wichtige Datenstrukturen wie `sk_buff` oder sockets, aber auch Makros die im Kernel verwendet werden.  
Weiterhin werden kurz ein paar Grundkonzepte von C vorgestellt die zum Verständnis benötigt werden (geht ganz schnell, versprochen!)

### Über mich

Ich bin Moritz, arbeite an der Uni im Bereich Netzwerktechnik. Mit Linux beschäftige ich mich schon seit längerem, aber erst seit kurzem mit dem Kernel selbst.  
Aktuell liegt mein Interesse besonders bei eBPF und dem Netzwerkstack.

