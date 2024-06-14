---
layout: talk
title:
permalink: /2024/programm/74-sicherer-fernzugriff-dank-linux-selbst-auf-ein-uraltes-windows/
weight:
menu:
---
## Sicherer Fernzugriff dank Linux - selbst auf ein uraltes Windows

### <img height = "32" src="../../../images/talk.svg"> 10:00 bis 10:50 in Raum V3 (A301)

### Stefan Baur

#### Abstract

Immer häufiger nutzen Ransomware-Gruppen statt Phishing-Mails schlecht abgesicherte  
Fernwartungszugänge als Einfallstor, um in Unternehmen einzudringen und alle Daten zu  
verschlüsseln.  
Wir zeigen, wie man Fernzugriffe mit aktueller Verschlüsselungstechnik und Zwei-Faktor-Authentisierung absichern kann - selbst wenn man auf ein uraltes Windows zugreifen muss.

#### Beschreibung

In diesem Vortrag zeigen wir verschiedene Fernzugriffs-Techniken, unter anderem auch mehrere  
Möglichkeiten, wie man mit einem zwischengeschalteten Linuxsystem von einem aktuellen  
PC aus sogar auf ein altes Windows XP sicher aus der Ferne zugreifen kann - ohne VPN,  
und auf Wunsch sogar portabel vom USB-Stick, ohne Softwareinstallation.  
Wir beginnen damit, wie man einen SSH-Server auf einem Raspberry Pi aufsetzt und diesen per  
Zwei-Faktor-Authentisierung absichert.  
Darauf aufbauend zeigen wir, wie man sich von diesem auf einen X2Go-Server "weiterhangeln"  
kann, aber auch, wie man diesen Raspberry Pi selbst zum X2Go-Server machen kann, um sich von  
dort auf Windows-Systeme zu verbinden.  
Die letzte Komponente ist der Aufruf des X2GoClients, der auch als "Portable Application", von einem USB-Stick, an einem beliebigen Windows-PC gestartet werden kann - oder man bootet von diesem Stick unser X2Go-Thin-Client-Image.

### Über mich

Stefan Baur, Jahrgang 1977, ist der aktuelle Projektmanager und Lead Evangelist des Open-  
Source-Projekts X2Go und geschäftsführender Gesellschafter der BAUR-ITCS UG
(haftungsbeschränkt), welche Support für X2Go anbietet, sowie der 1. Vorsitzende der Open  
Remote Computing Association - orca e.V., einem Dachverein für freie Remote-Computing-  
Projekte

