---
layout: talk
title:
url: /2026/programm/196-delegacy-erzwinge-ipv6-im-groen-stil/
weight:
menu:
---
## DeLegacy: Erzwinge IPv6 im großen Stil

### <img height = "32" src="../../../images/talk.svg"> 13:00 bis 13:50 in Raum V5 (C215)

### Mynacol

#### Abstract

Erfahre, wie du den Anteil von IPv6-Verkehr erhöhen kannst, indem du DNS‑Antworten manipulierst und wie du X/Twitter und Discord dazu bringst, IPv6 zu unterstützen _(es gelten Einschränkungen)_.

#### Beschreibung

Content Delivery Networks (CDNs) erzeugen viel Traffic, und fast alle unterstützen IPv6. Dennoch fehlen vielen Webseiten, die diese CDNs nutzen, IPv6-Adressen. Werden sie jedoch über die passende IPv6-Adresse angesprochen, funktionieren sie ohne Probleme. Durch gezielte DNS-Manipulationen lässt sich die Anzahl der Domains mit IPv6 so deutlich steigern. Zu diesem Zweck habe ich das [DeLegacy RPZ Projekt](https://codeberg.org/IPv6-Monostack/delegacy-rpz) entwickelt.  
Dieser Vortrag erläutert die zugrunde liegenden Mechanismen und wie sie für diesen Zweck genutzt werden. Er zeigt, wie populäre DNS-Server wie BIND oder Unbound so konfiguriert werden können, dass sie diese Aufgabe übernehmen, statt eine weitere Software zu benötigen. Ich erkläre, wie sich DNS [Response Policy Zones](https://dnsrpz.info/), [DNAMEs](https://de.wikipedia.org/wiki/DNAME_Resource_Record) und [DNS64](https://de.wikipedia.org/wiki/NAT64#DNS64) einsetzen lassen, um die beabsichtigten Manipulationen umzusetzen. Außerdem stelle ich meinen Ansatz vor, wie nützliche Domains und IP-Adressen beim Erstellen neuer Regeln identifiziert und getestet werden. Abschließend präsentiere ich Statistiken zur gestiegenen IPv6-Verbreitung auf Basis der [Tranco-Liste](https://tranco-list.eu/).

### Über mich

Hacker, der sich für Self-Hosting, Sicherheit, Privatsphäre, NixOS und IPv6 interessiert. Du findest mich im [Fediverse](https://social.mynacol.xyz/mynacol).

