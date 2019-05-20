---
layout: talk
title:
permalink: /2019/programm/harald-koenig-den-flaschenhals-in-einer-langsamen-pipe-optimieren-durch-parallelisierung/
weight:
menu:
---
## Den Flaschenhals in einer langsamen Pipe optimieren durch Parallelisierung

### <img height = "32" src="../../../images/talk.svg"> 12:00 bis 12:50 in Raum V3

### Harald König

Neues aus meiner Shell-Küche: in einem Skript zum Disassemblieren eines einfachen seriellen Protokolls mit Hilfe von "sed" werden die Input-Daten immer größer und sed braucht immer länger -- inzwischen bei letzten Messdaten über 20 Minuten! Das muss doch auch schneller gehen?!

Heute haben (fast) alle Rechner mehrere CPU-Cores und (Hyper)Threads. Warum also läuft das zu langsame sed nicht parallel auf allen verfügbaren CPUs und vervielfacht so den Durchsatz des Tools ?

Klingt einfach, ist aber zunächt gar nicht sooo trivial alleine mit Shell-Mitteln.  Die Probleme werden gezeigt, und wie man mit ein bissl Aufwand das alles in den Griff bekommen kann.

Und dann gibt es noch ein tolles Kommandozeilen-Tool, welches genau diese Parallelisierung eines Programms wie sed in einer Pipe mit allen seinen Problemen perfekt löst, ganz ohne die grauen Haare der "nur-in-Shell-Lösung".

### Vorwissen

wie immer: tippen können.  
und vielleicht ein bissl Spass mit oder zumind. Interesse an der Kommandozeile und Pipes.

### Über mich

Physik-Studium in Tübingen, Rechner und DCF77 seit ~1980, (La)TeX seit 1986, UNIX seit ~1987, Linux seit 1992 (0.98.4), XFree86-Treiber für S3 von ~1993-2001. Von 2001 bis 2014 bei der science+computing ag in Tübingen (heute Atos) als SW-Entwickler. Seit 2014 nun bei Bosch Sensortec GmbH in Kusterdingen/Reutlingen als “System Expert” für Linux, Android und uC Treiber.

