---
layout: talk
title:
url: /2016/programm/arnd-bergmann-2038-alles-ist-kaputt/
weight:
menu:
---
## 2038 - alles ist kaputt

### <img height = "32" src="../../../images/lightning.svg"> 12:15 bis 12:20 in Raum V3 {#-1215-bis-1220-in-raum-v3}

### Arnd Bergmann

Zeit wird in Unix und Linux in time_t beschrieben, oft eine 32-bit Zahl, die Sekunden zwischen 1970 und 2038 zählt. Wir arbeiten daran, das Grundsätzlich auf 64 bit zu erweitern, damit es auch 2039 noch funktionierende Computer gibt.

### Links

- <a href="http://kernelnewbies.org/y2038" target="_blank">http://kernelnewbies.org/y2038</a>
- <a href="https://lwn.net/Articles/643234/" target="_blank">https://lwn.net/Articles/643234/</a>
