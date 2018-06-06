---
layout: talk
title:
permalink: /2018/programm/lukas-kallies-linux-server--und-desktop-lifecycle-management/
weight:
menu:
---
## Linux Server- und Desktop-Lifecycle-Management

### <img height = "32" src="../../../images/workshop.svg"> 12:00 bis 13:50 in Raum W1

### Lukas Kallies

Eine große Anzahl an Linux-Systemen zu verwalten und die Software darauf aktuell zu halten stellt eine Herausforderung dar. Nicht selten wird dies durch Lücken (Spectre/Meltdown, Heartbleed, Shellshock, um einige der jüngsten und bekanntesten zu nennen) in zentralen Bestandteilen in Erinnerung gerufen. An dieser Stelle kommen Lifecycle-Management (LCM) Lösungen wie Katello (Basis für Red Hats Satellite 6) ins Spiel. Anhand von Katello wird das Patchmanagement von Linux-Hosts vorgestellt. Zudem werden weitere Bestandteile von Katello wie Deployment, Subscription Management und die Einbindung von Compute Ressource Providern (VMware, RHV oder auch Cloud Dienstleister) vorgestellt.

### Vorwissen

Grundlegendes Know-How in der Administration von Linux-Systemen sollte vorhanden sein. Teilnehmer werden gebeten einen Laptop mitzubringen, auf dem Vagrant installiert und konfiguriert ist. Zwei virtuelle Maschinen sollten darauf lauffähig sein. Im Workshop wird Forklift verwendet, um Katello zu installieren und zu verwalten. Ein vorgängiges `vagrant up centos7-katello-3.6` ist für den Workshop hilfreich.

### Über mich

Jahrgang 1983, verheiratet, zwei Kinder Informatikstudium an der Hochschule Furtwangen Senior System Engineer im Bereich Linux, Lifecycle- und Configurationmanagement bei Puzzle ITC in Zürich

### Links

- <a href="https://lukex.de/" target="_blank">Lukas Kallies</a>
- <a href="https://www.vagrantup.com/" target="_blank">Hashicorp Vagrant</a>
- <a href="https://github.com/theforeman/forklift/" target="_blank">Forklift (Katello Deployment Script)</a>
- <a href="https://theforeman.org/plugins/katello/" target="_blank">Katello (Foreman Plugin)</a>
- <a href="https://theforeman.org/plugins/" target="_blank">Foreman Plugins</a>
