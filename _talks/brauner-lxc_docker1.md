---
layout: talk
title:
permalink: /programm/brauner-lxc_docker1/
weight: 
menu:
---
## Operating-system-level&nbsp;virtualization

### <img height = "32" src="../../images/talk.svg"> 10:00 bis 11:00 in Raum V1

### Christian&nbsp;Brauner

Hands-on Einführung in operating-system-level virtualization.

1. Technische Grundlagen: Implementierung und Möglichkeiten im/des Kernels:
  - Wie funktionieren cgroups?
  - Was kann man mit ihnen machen?
  - Was ist namespace isolation?
  - Was sind linux capabilities?

2. Use-case 1 (Workflow):
  - Wie konfiguriere und nutze ich low-level container virtualization tools wie lxc, für software development?
  - Was sind die Vorteile?

3. Use-case 2 (Sandboxing-Security):
  - Operating-system-level virtualization zum sandboxing proprietärer software mit grafischen output, GPU-access (Hardware access auf dem Host im allgemeinen) (z.B. Google Chrome im Container)
  - Einführung in unpriviligierte Container, die user namespaces nutzen

### Vorwissen 

- Umgang mit dem Terminal und den grundlegenden Tools: chmod, chown, sed etc.
- C-basics (wirklich wenig)
- basic shell-scripting in sh und bash
- git

### Vorbereitung

- Kernel-Version >= 3.13
- lxc >= 1.1.0
- lxcfs 0.7
- cgmanager 0.36
- git

 "We're trying to extend our interfaces to the point that you can safely run
 code that you traditionally absolutely could not as root."
Linus Torvalds, on namespaces and container security. (Linux Kernel Developer Panel)

### Links

- <a href="https://en.wikipedia.org/wiki/Operating-system-level_virtualization" target="_blank">en.wikipedia.org/wiki/Operating-system-level_virtualization</a>
- <a href="https://en.wikipedia.org/wiki/LXC" target="_blank">en.wikipedia.org/wiki/LXC</a>
- <a href="https://github.com/lxc/lxc" target="_blank">github.com/lxc/lxc</a>
- <a href="https://en.wikipedia.org/wiki/Sandbox_%28computer_security%29" target="_blank">en.wikipedia.org/wiki/Sandbox_(computer_security)</a>
- Namespace Isolation: MOUNT-, PID-, UTSNAME-, IPC-, NETWORK-, und USER-Namespaces: <a href="http://man7.org/linux/man-pages/man7/namespaces.7.html" target="_blank">man7.org/linux/man-pages/man7/namespaces.7.html</a>
- <a href="https://en.wikipedia.org/wiki/Cgroups" target="_blank">en.wikipedia.org/wiki/Cgroups</a>
- Linux capabilities: <a href="http://linux.die.net/man/7/capabilities" target="_blank">linux.die.net/man/7/capabilities</a>
