---
layout: talk
title:
url: /2023/programm/71-killing-in-the-name-of-ebpf/
weight:
menu:
---
## Killing in the name of eBPF

### <img height = "32" src="../../../images/lightning.svg"> 16:10 bis 16:15 in Raum V3 {#-1610-bis-1615-in-raum-v3}

### Cedric Casper

In "Bring Your Own Code"-Szenarien wird den vom Benutzer bereitgestellten Containern ("Bring Your Own Container") häufig wenig bis gar nicht vertraut, weshalb zusätzliche Schutzmaßnahmen aktiviert werden. Dazu gehören u.a. Seccomp-Profile. Seccomp kann verwendet werden, um Prozesse in einem Container einzuschränken, indem bestimmte festgelegte System Calls diesem verweigert werden. Um diese Möglichkeit zu erweitern, wurde ein auf eBPF basierendes Programm geschrieben, das entsprechende Verstöße gegen ein Seccomp Profil erkennt und den entsprechenden Podman-Container beendet. Dieses Programm soll kurz erläutert werden.

### Vorwissen

Man sollte wissen, was Container (z.B. Docker, Podman) sind und ggf. schon mal von Seccomp gehört oder es angewendet haben.

### Über mich

Ich mag Container.

