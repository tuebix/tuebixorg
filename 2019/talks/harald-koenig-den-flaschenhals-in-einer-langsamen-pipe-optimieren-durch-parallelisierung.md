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

Neues aus meiner Shell-Kueche: in einem Skript zum Disassemblieren eines einfachen seriellen Protokolls mit Hilfe von "sed" werden die Daten immer groesser und sed  braucht immer laenger -- inzwischen bei letzten Messungen ueber 20 Minuten! Das muss doch auch schneller gehen?!

Heute haben (fast) alle Rechner mehrere CPU-Cores und (Hyper)Threads, warum also laeuft das zu langeame sed nicht parallel auf allen verfuegbaren CPUs und verfielfacht so den Durchsatz des Tools ?

Klingt einfach, ist aber zunaecht gar nicht sooo einfach mit Shell-Mitteln.  Die Probleme werden gezeigt, und wie man mit ein bissl aufwand das alles in den Griff bekommen kann.

Und dann gibt es noch ein tolles Kommandozeilen-Tool welches genau diese Parallelisierung eines Programms wie sed in einer Pipe mit allen seinen Problemen perfekt loest, ganz ohne die grauen Haare der "nur-in-Shell-Loesung".

### Vorwissen

wie immer: tippen koennen.
und vielleicht ein bissl Spass mit oder zumind. Interesse an der Kommandozeile und Pipes.

### Über mich

Physik-Studium in Tübingen, Rechner und DCF77 seit ~1980, (La)TeX seit 1986, UNIX seit ~1987, Linux seit 1992 (0.98.4), XFree86-Treiber fuer S3 von ~1993-2001. Von 2001 bis 2014 bei der science+computing ag in Tuebingen (heute Atos) als SW-Entwickler. Seit 2014 nun bei Bosch Sensortec GmbH in Kusterdingen/Reutlingen als “System Expert” fuer Linux , Android und uC Treiber.

