---
layout: talk
title:
url: /2026/programm/200-wie-sicher-ist-systemd-wirklich/
weight:
menu:
---
## Wie sicher ist systemd wirklich?

### <img height = "32" src="../../../images/talk.svg"> 11:30 bis 12:20 in Raum V1 (F119)

### Dr. Christoph Zimmermann

#### Abstract

Wie sicher ist systemd wirklich?

Kaum eine andere Komponente des Linux-Ökosystems hat seit ihrer Einführung mehr Kontroversen erfahren als systemd, von technischer Kritik wie Benutzung von Binärformaten für Logging-Aspekte bis hin zur vollständigen Elimination wie z. B. Devuan, ein Debian-Spin welcher explizit auf systemd verzichtet. 

Ursprünglich gedacht als Ersatz für das in die Jahre gekommene SystemV-Init hat systemd mittlerweile einen Funktionsumfang erreicht, der von einem flexiblen Init-System über Namensauflösung, Hypervisor-/Container-Funktionen bis hin zur Unterstützung von Benutzerkonten über Maschinengrenzen hinweg reicht.

Ziel des Vortrags ist ein Überblick über die Sicherheitsaspekte von systemd - von einer Analyse des Quellcodes über über Angriffsoberflächenanalyse (inkl. Common Vulnerability and Exposures, CVEs) von systemd bis hin zur Github-Metriken, die über die Issue Resolution, etc. Auskunft geben. Der Fokus liegt hierbei neben der reinen Präsentation von Inhalten auf dem Erfahrungsaustausch unter den Zuhörern jenseits der Fragen im Anschluß an die Präsentation.

Der Vortrag gliedert sich wie folgt:

- Hintergrund / Einordnung,  
- Wesentliche Komponenten / Architektur,  
- Software-Qualität der Implementierung,  
- Analyse der Sicherheit der Codebasis,  
- Code-/Github-Metriken,  
- Publikumsdiskussion,  
- Ausblick.

### Über mich

Graubärtiger FLOSS-Hacker ohne Bart, besessen von Open-Source-Betriebssystemen und anderen Hipster-Themen.

Meine erste Begegnung mit den FLOSS-Technologien war 1987, als ich einen Editor namens Emacs kompilierte. Diese Begegnung hatte einen bleibenden Effekt, so dass ich mich mehr als dreißig Jahre später immer noch mit FLOSS-Ökosystemen, -Technologien und -Gemeinschaften sowohl aus technischer als auch aus gesellschaftlicher und politischer Sicht beschäftige. Ich bin Vorstandsmitglied einer der größten deutschen Linux User Groups und regelmäßiger Referent auf deutschen und internationalen FLOSS-Veranstaltungen. Zusammen mit Martin Visser moderiere ich einen der am schnellsten wachsenden FLOSS-Podcasts namens Linux Inlaws. Zu anderen Hobbies gehören IT-Sicherheit, anderer Leute Computer, alles was mit Software-Entwicklung zu tun hat und andere Formen der schwarzen Kunst :-).

