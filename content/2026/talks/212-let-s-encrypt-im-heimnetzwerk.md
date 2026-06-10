---
layout: talk
title:
url: /2026/programm/212-let-s-encrypt-im-heimnetzwerk/
weight:
menu:
---
## Let's Encrypt im Heimnetzwerk

### <img height = "32" src="../../../images/talk.svg"> 15:00 bis 15:50 in Raum V5 (C215)

### Robert Scheck

#### Abstract

SSL/TLS-Zertifikate über ACME lassen sich auch in nicht öffentlich erreichbaren Netzwerken (Heim- oder Firmennetzen) einsetzen. Erläutert werden, neben der Funktionsweise, praxisnahe Lösungsansätze am Beispiel der kostenlosen Zertifizierungsstelle „Let's Encrypt“.

#### Beschreibung

Egal ob [Certbot](https://certbot.eff.org/) der Electronic Frontier Foundation (EFF), [dehydrated](https://dehydrated.io/), [acme.sh](https://github.com/acmesh-official/acme.sh) oder ein anderer ACME-Client verwendet wird: [Let's Encrypt](https://letsencrypt.org/de/) ermöglicht die schnelle und unkomplizierte Ausstellung kostenloser SSL/TLS-Zertifikate für gemietete Root-Server oder virtuelle Maschinen bei Hosting-Anbietern. Auch im geschäftlichen Umfeld hat sich Let's Encrypt inzwischen etabliert. In der Praxis wird der Dienst jedoch meist auf öffentlich über das Internet erreichbaren Servern eingesetzt.

Doch wie lassen sich SSL/TLS-Zertifikate von Let's Encrypt in einem Heimnetzwerk (oder auch einem internen Firmennetz) nutzen, das nicht öffentlich erreichbar ist? Gerade im heimischen Intranet betreibt man häufig Dienste auf einem Single-Board-Computer – etwa einem Raspberry Pi – wie Pi-hole, ownCloud/Nextcloud bzw. OpenCloud, einen kleinen Webserver oder eine Groupware unter einer eigenen (Familien-)Domain. Diese Systeme sind jedoch in der Regel nicht direkt aus dem Internet erreichbar, sondern nur intern oder über ein VPN zugänglich.

Der Vortrag beleuchtet die Funktionsweise der „Challenges“ im ACME-Standard und zeigt anschließend konkret entsprechende Konfigurationsmöglichkeiten auf. Die vorgestellten Möglichkeiten beschränken sich nicht auf Let's Encrypt sondern können auch mit automatisierungsfreundlichen kommerziellen Zertifizierungsstellen für OV/EV-Zertifikaten umgesetzt werden.

### Über mich

Langjähriger Contributor beim Fedora-Projekt, z.B. als Paket-Maintainer, Ambassador und Mentor, sowie Mitwirkender bei diversen anderen Open-Source-Projekten – mit Interesse an IPv6 und (öffentlichen) Netzwerken.

