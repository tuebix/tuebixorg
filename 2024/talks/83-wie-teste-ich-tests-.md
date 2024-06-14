---
layout: talk
title:
permalink: /2024/programm/83-wie-teste-ich-tests-/
weight:
menu:
---
## Wie teste ich Tests?

### <img height = "32" src="../../../images/talk.svg"> 13:00 bis 13:50 in Raum V3 (A301)

### Peter Hrenka

#### Abstract

Langsam hat es sich herumgesprochen, dass man Software testen sollte und OpenSource Projekte gehen auch oft mit gutem Beispiel voran.

Aber wann ist ein Test denn ein guter Test? Wenn er 100% Coverage hat?  
Leider taugt Coverage nicht als alleiniges Gütekriterium weshalb man noch etwas anderes braucht.  
Ich stelle die Idee des "adversarial testing" vor, das mit (relativ) einfachen Mitteln eine Verbesserung der Test-Qualität erreichen kann.

#### Beschreibung

Die Grundidee ist recht einfach: Ein guter Test muss "gute" von "schlechten" Programmen unterscheiden können. Wenn man nun die Test-Infrastruktur so aufbaut, dass man beliebige Funktionen und Klassen mit demselben Test prüfen kann, kann man mit recht trivialen "bösartigen Implementierungen" ungeeignete Tests entlarven und anschließend verbessern.  
In dem Vortrag werde ich einige Beispiele zeigen, wie man das "adversarial testing" mit einem leicht modifizierten googletest praktisch an einem C++-Programm durchführen kann.

#### Vorwissen

C/C++ Grundwissen, Grundwissen Softwaretest.

### Über mich

Ich habe in Tübingen Informatik und Mathematik studiert und verwende fast ebensolange schon Linux in allen Lebenslagen. Mit einer kurzen Unterbrechung war ich auch in der Lage, Linux auch in meiner beruflichen Umgebung einzusetzen.

Ich nicht gerade arbeite, funke oder Klavier spiele, besuche ich C++ und OpenSource Konferenzen.

