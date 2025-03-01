---
layout: talk
title:
url: /2018/programm/holger-gantikow-do-containers-still-not-contain-what-s-new-in-container-security/
weight:
menu:
---
## Do Containers still not contain? What's new in Container Security

### <img height = "32" src="../../../images/talk.svg"> 14:00 bis 14:50 in Raum V2 {#-1400-bis-1450-in-raum-v2}

### Holger Gantikow

Der Vortrag gibt einen kurzen Überblick über den aktuellen Stand der Containertechnologie und setzt den Fokus darauf, was hier mit Hinblick auf Sicherheitsaspekte zu beachten ist, bzw. was sich zur Absicherung von containerisierten Infrastrukturen einsetzen lässt.  Beim Vortrag handelt es sich um ein erweitertes Update des TUEBIX2017-Talks [0], bei dem unter anderem Werkzeuge und Technologien wie Seccomp Profiles [1], User Namespaces (Phase 1) [2], Authorization Plugins [3], aber auch SELinux, AppArmor und Image Vulnerability Scanner [4,5], sowie Docker Bench for Security [6] vorgestellt wurden.  Zusätzlich zu diesen Werkzeugen gibt es inzwischen eine Reihe von Forschungsprojekten, welche die Basiswerkzeuge funktional erweitern, beispielsweise LiCShield [7] als AppArmor-Erweiterung, SPEAKER [8], das mittels Seccomp-Filter unterschiedliche SysCalls zur Startup- und Laufphase eines Containers zulässt und somit die Anzahl der zur Verfügung stehenden SysCalls für manche Szenarien deutlich verringern kann.  Auch existieren Ansätze und Werkzeuge [9], die sich zur Erkennung von Anomalien einsetzen lassen. Sie nutzen den Vorteil, dass, bedingt durch die Natur der Container, die Überwachung direkt auf dem Host sehr detaillierte Infos über den Containerzustand liefern, ohne dass hierzu wie bei VMs zusätzliche Komponenten notwendig wären. Im Zuge des Vortrags werden diese und weitere Technologien kurz vorgestellt und es wird betrachtet, was zu beachten ist, um Container in eine verteilte Umgebung mit Sicherheitsanforderungen einzubinden. Besonderes Augenmerk liegt auf dem Themenkomplex "Image Security" [10] und auf aktuellen Ansätzen die "ab Werk" verfügbare Werkzeuge sinnvoll erweitern, sowie zur Anomalieerkennung eingesetzt werden können.

Links/Weiterführendes:
- [0] [TUEBIX2017: Containing Containers? - oder “Wie lässt sich der Wal bändigen?”](https://www.tuebix.org/2017/programm/holger-gantikow-containing-containers-oder-wie-laesst-sich-der-wal-baendigen/)
- [1] [Seccomp security profiles for Docker](https://docs.docker.com/engine/security/seccomp/)
- [2] User Namespaces:
  * [Phil Estes - Rooting out Root: User namespaces in Docker](https://events.static.linuxfound.org/sites/events/files/slides/User%20Namespaces%20-%20ContainerCon%202015%20-%2016-9-final_0.pdf)
  * [User Namespaces: 2017 Status Update and Additional Resources](https://integratedcode.us/2017/02/24/user-namespaces-2017-status-update-and-additional-resources/)
- [3] [twistlock/authz - Docker Authorization Plugin](https://github.com/twistlock/authz)
- [4] [Docker - Docker Security Scanning](https://docs.docker.com/docker-cloud/builds/image-scan/)
- [5] [coreos/clair - Vulnerability Static Analysis for Containers](https://github.com/coreos/clair)
- [6] [docker/docker-bench-security](https://github.com/docker/docker-bench-security)
- [7] Mattetti, M., Shulman-Peleg, A., Allouche, Y., Corradi, A., Dolev, S., & Foschini, L. (2015). Securing the infrastructure and the workloads of linux containers.
- [8] Lei, L., Sun, J., Sun, K., Shenefiel, C., Ma, R., Wang, Y., & Li, Q. (2017). SPEAKER: Split-phase execution of application containers. In Lecture Notes in Computer Science (Vol. 10327)
- [9] Anomaly Detection:
  * Abed et al., (n.d.). Applying Bag of System Calls for Anomalous Behavior Detection of Applications in Linux Containers.
  * Abed, A. et al., (2015). Intrusion Detection System for Applications Using Linux Containers. Security and Trust Management
  * https://www.sysdig.org
  * https://www.sysdig.org/falco/
- [10] Shu, R., Gu, X., & Enck, W. (2017). A Study of Security Vulnerabilities on Docker Hub. In Proceedings of the Seventh ACM on Conference on Data and Application Security and Privacy - CODASPY ’17

### Vorwissen

Ein spezielles Vorwissen der Zuhörer wird nicht vorausgesetzt. Interesse an Virtualisierung, Containern und der gegebenen Problemstellung ist sicherlich von Vorteil, um eine rege Diskussion und Erfahrungsaustausch zu gewährleisten ;)

### Über mich

Holger Gantikow hat an der Hochschule Furtwangen Informatik studiert und ist bei Atos (ehemals science + computing ag) in Tübingen als Senior Systems Engineer tätig. Dort beschäftigt er sich mit der Komplexität heterogener Systeme im CAE-Berechnungsumfeld und betreut Kunden aus dem technisch-wissenschaftlichen Bereich.

