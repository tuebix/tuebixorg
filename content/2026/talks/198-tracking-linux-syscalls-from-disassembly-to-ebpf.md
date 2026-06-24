---
layout: talk
title:
url: /2026/programm/198-tracking-linux-syscalls-from-disassembly-to-ebpf/
weight:
menu:
---
## Tracking Linux Syscalls: From Disassembly to eBPF

### <img height = "32" src="../../../images/talk.svg"> 14:00 bis 14:50 in Raum V5 (C215)

### Stefan

#### Abstract

Was macht ein Linux-System eigentlich im Alltag?  
Dieser informelle Vortrag nähert sich der Frage im Hinblick auf eine wichtige Abstraktionsebene: der Schnittstelle zwischen Anwendersoftware und Kernel -- die Systemaufrufe (Syscalls).

Nach einer kurzen Übersicht wie Syscalls unter Linux auf x86-64 definiert sind und aufgerufen werden, nähern wir uns einer Antwort aus zwei Perspektiven:

Mit *statischer* Analyse (Disassembly) lässt sich abschätzen, welche Syscalls Programme grundsätzlich verwenden könnten (abgesehen von z.B. Ungenauigkeiten beim Disassemblieren, und von dynamisch zur Laufzeit berechneten Syscall-Nummern).

Mit *dynamischer* Analyse (hier mittels eBPF) lässt sich im Vergleich zu statischer Analyse messen, welche Syscalls tatsächlich über einen längeren Zeitraum von einem System ausgeführt werden.

Der Vortrag gibt Einblick in praktische Systemintrospektion und zeigt, welche Syscalls bei typischen Paketen auf Debian von Compilern verwendet und tatsächlich zur Laufzeit häufig ausgeführt werden.

### Über mich

Seit 2021 arbeite ich bei der SySS GmbH in Tübingen und beschäftige mich dort hauptberuflich mit der Sicherheit von internen Unternehmensnetzwerken, mit einem Fokus auf Windows / Active Directory Umgebungen.  
Darüber hinaus bin ich auch in meiner Freizeit breit an technischen Themen interessiert und nutze natürlich auch Linux.

