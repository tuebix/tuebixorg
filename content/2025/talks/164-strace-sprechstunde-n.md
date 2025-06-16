---
layout: talk
title:
url: /2025/programm/164-strace-sprechstunde-n/
weight:
menu:
---
## STRACE-Sprechstunde(n)

### <img height = "32" src="../../../images/workshop.svg"> 10:00 bis 11:50 in Raum W2 (A302)

### Harald König

#### Abstract

Was ich schon immer mit STRACE machen & diskutieren wollte -- iIhr fragt, ich erzähle und trace...

An euren Fragen, Themen und Problemen (oder doch nur meine eigenen Lösungen?) werde ich einige Grundlagen von STRACE erörtern und helfen, neue Ideen zu bekommen…

Am besten natürlich über EURE Probleme, daher bitte im VORAUS mit interessanten Themen melden an: koenig (at) linux.de

#### Beschreibung

strace ist ein wahres Wundertool in Linux, man muss es nur einsetzen – und kann damit sehr viel  
über die Abläufe und Interna von Linux lernen. Mit strace können einzelne oder mehrere Prozesse zur Laufzeit auf System-Call-Ebene ”beobachtet“ werden. Damit lassen sich bei vielen Problemen  
sehr einfach wertvolle Informationen zum Debuggen gewinnen: welche Config-Dateien wurden wirklich gelesen, welches war die letzte Datei oder Shared-Library vor dem Crash usw. Im Unterschied  
zu interaktiven Debuggern läuft das zu testende Programm mit strace mehr oder weniger in Echtzeit ab, und man erhält schon während des Programm-Laufs jede Menge Ausgaben zu allen erfolgten  
Kernel-Calls, so dass man den Ablauf des Prozesses ”live“ mitverfolgen bzw. den abgespeicherten  
Output nachträglich bequem auswerten kann.  
Auch bei Performance-Problemen kann man mit strace interessante Informationen gewinnen: wie  
oft wird ein Syscall ausgeführt, wie lange dauern diese, wie lange ”rechnet“ das Programm selbst  
zwischen den Kernel-Calls. Man kann auch den kompletten I/O eines Programms (Disk oder Net) mit  
strace recht elegant mitprotokollieren und später offline analysieren (oder auch ”replay“en, bei Bedarf sogar in ”Echtzeit“ Dank präziser Time-Stamps).

Der Workshop soll anregen, strace kennen zulernen, und neue Ideen im Umgang mit strace zu bekommen (das gilt natürlich auch für durch eure Fragen;-)

Auf diesen alten Folien (https://www.luga.de/download/Vortraege/lit2016-strace.pdf) gibt es ab Seite 10 so einiges über strace zu schmökern...

### Über mich

Physik-Studium in Tübingen,  
Rechner und DCF77 seit ~1980, (La)TeX seit 1986,  
UNIX seit ~1987,  
Linux seit 1992 (0.98.4),  
XFree86-Treiber fuer S3 von ~1993-2001.  
Von 2001 bis 2014 bei der science+computing ag in Tuebingen als SW-Entwickler.  
Seit 2014 nun bei Bosch Sensortec GmbH in Kusterdingen/Reutlingen als “System Expert” fuer Linux (DevOps) und embedded Android (Treiber).

Weitere Interessen sind u.a. Reisen, Kernel, System-Technik und -Tools, Hardware, Grafik (-Treiber,-HW), neuerdings mal wieder Embedded-Systeme und Messtechnik, GPS und OpenStreetmap, u.v.a.m…..

