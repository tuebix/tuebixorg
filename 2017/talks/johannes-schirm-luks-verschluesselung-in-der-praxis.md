---
layout: talk
title:
url: /2017/programm/johannes-schirm-luks-verschluesselung-in-der-praxis/
weight:
menu:
---
## LUKS-Verschlüsselung in der Praxis

### <img height = "32" src="../../../images/talk.svg"> 13:00 bis 13:30 in Raum V3 {#-1300-bis-1330-in-raum-v3}

### Johannes Schirm

Eines der Themen, die mich während meines Umstiegs auf Linux am meisten begeistert haben, ist die Datenträgerverschlüsselung unter Linux. In diesem Kurzvortrag möchte ich kompakt zusammenfassen, was ich über das Kernelmodul dm_crypt und den LUKS-Standard in Erfahrung bringen konnte. Nach einem kurzen theoretischen Teil folgt eine Demonstration, in der ich zeigen möchte, wie sich ein Datenträger mit wenigen Befehlen bombensicher verschlüsseln lässt. Dabei liegt der Fokus auf der ausführlichen Erklärung der Vorgänge, sodass jeder Zuhörer zu Hause gleich selbst mit dem Verschlüsseln loslegen kann. Im Anschluss geht es noch um einige Tricks, mit denen man gegen einen kleinen Teil der gewonnenen Sicherheit bei Bedarf die Alltagstauglichkeit erhöhen kann. Dabei wird ein zweiter Datenträger als Schlüsseldatenträger verwendet und es wird ein kurzer Blick auf das udev-System für die einfache und sichere Automatisierung geworfen.

### Vorwissen

Außer einer groben Vorstellung von Dateisystemen, Partitionierung und Geräten unter Linux dürfte kein spezielles Vorwissen nötig sein, da ich durch den theoretischen Teil und die Demonstration ein möglichst klares Bild der Vorgänge auf praktischer Ebene vermitteln möchte.

### Über mich

Ich bin Student der Medien- und Kommunikationsinformatik in Reutlingen und arbeite gerade an meiner Bachelorthesis. Seit Anfang 2016 interessiere ich mich seit meines Umstiegs auf Linux sehr für das Themengebiet freier und quelloffener Software und durfte schon eine Menge interessanter Dinge lernen. Das Finden von alltagstauglichen und eleganten IT-Lösungen ist neben dem Klavierspielen, Filme Produzieren und Videospiele Spielen Teil meiner Freizeit.

### Links

- <a href="https://linux.die.net/man/8/cryptsetup" target="_blank">Manpage zu Cryptsetup</a>
- <a href="https://wiki.ubuntuusers.de/udev/#Beispiele-fuer-eigene-Regeln" target="_blank">Einige Szenarien für Automatisierung mit dem udev-System</a>
- <a href="https://de.wikipedia.org/wiki/Device_Mapper" target="_blank">Übersicht zum Mappen von Geräten unter Linux</a>
- <a href="http://www.linux-community.de/Internal/Artikel/Print-Artikel/LinuxUser/2009/02/USB-Sticks-verschluesseln" target="_blank">Einfacher Weg zum verschlüsselten Datenträger</a>