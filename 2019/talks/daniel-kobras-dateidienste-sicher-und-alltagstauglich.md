---
layout: talk
title:
permalink: /2019/programm/daniel-kobras-dateidienste-sicher-und-alltagstauglich/
weight:
menu:
---
## Dateidienste - sicher und alltagstauglich

### <img height = "32" src="../../../images/talk.svg"> 12:00 bis 12:50 in Raum V4

### Daniel Kobras

Administratoren stehen regelmäßig im Spannungsfeld zwischen
Sicherheit, Schnelligkeit und Nutzbarkeit ihrer Dienste. In der Praxis
sind Kompromisse an der Tagesordnung.  Der Vortrag präsentiert eine
Übersicht sicherer Dateidienste auf Basis von Kerberos, vergleicht den
Funktionsumfang und zeigt Lösungswege für den Alltag, die die
Nutzbarkeit der Dienste wahren, ohne Sicherheit und Schnelligkeit aufs
Spiel zu setzen.

NFS und SMB, aber auch einige spezielle Dateisysteme wie Lustre, setzen auf Kerberos, wenn es um das Thema Sicherheit geht. Neben der starken
Authentisierung sorgt Kerberos auch für Integrität und Vertraulichkeit der
Nutzdaten. In der Praxis führt die Anforderung nach starker Authentisierung
häufig zu Widersprüchen, wenn Prozesse auch ohne Nutzerinteraktion ablaufen sollen. Beispiele wären Batch-Prozesse, HPC-Jobs und andere Netzwerkdienste mit kerberisiertem Datenzugriff.

Diese Diskrepanz verhindert den Einsatz von Kerberos in Verbindung mit solchen Netzdateisystemen aber nicht völlig. Der Vortrag stellt verschiedene
Kompromisse vor, die auch nicht-interaktiven Prozessen den sicheren Zugriff
erlauben. Allerdings sind hier Randbedingungen zu beachten, denn nicht jede
Implementierung spielt reibungslos mit jedem Verfahren zusammen. Welche
Kombinationen in der Praxis funktionieren, zeigt dieser Vortrag.

### Vorwissen

Grundkenntnisse zu Kerberos und Netzdateisystemen sind hilfreich.

### Über mich

Daniel Kobras ist Principal Architect bei Puzzle ITC Deutschland. Zu seinen Schwerpunkten zählen Scale-out-Storage und sichere Dateidienste.

