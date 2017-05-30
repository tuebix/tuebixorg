---
layout: talk
title:
permalink: /2017/programm/christian-brauner-lxd/
weight:
menu:
---
## LXD

### <img height = "32" src="../../../images/talk.svg"> 23:00 bis 24:00 in Raum V7

### Christian Brauner

LXD is a container management tool built on top of LXC and offering a REST API to manage and interact with multiple container hosts over the network.  This talk will go over the main features of LXD, a pretty thorough demonstration of its abilities, a run through the work currently being done and end with questions.  LXD is a project which began a bit over a year ago, by the same team who built LXC.  It's building on top of the very stable LXC library and adds a whole network layer to it through a simple and clean REST API.  It's user experience was rethought from the ground up, favoring security and reliability, using every single kernel security feature available to provide a safe, yet extremely fast environment. Reliability is achieved through extended error handling and the use of container images in place of locally built container templates.  LXD focuses on infrastructure containers, that is, containers running a full Linux distribution exactly as you would in a virtual machine. It doesn't know about nor care about application containers (docker, rocket, ...). Those technologies are great to manage micro-services and are a good way to distribute software, as such they make a lot of sense, inside a LXD container.  More information on the LXD project can be found at: https://linuxcontainers.org/lxd The code may be found at: https://github.com/lxc/lxd And a fully feature, interactive demo of its capabilities here: https://linuxcontainers.org/lxd/try-it

### Über mich

LX{C,D} core dev. Also, this guy.

### Links

- <a href="https://linuxcontainers.org/lxd/try-it" target="_blank">https://linuxcontainers.org/lxd/try-it</a>
- <a href="https://linuxcontainers.org" target="_blank">https://linuxcontainers.org</a>
- <a href="https://github.com/lxc/lxc" target="_blank">https://github.com/lxc/lxc</a>
- <a href="https://github.com/lxc/lxd" target="_blank">https://github.com/lxc/lxd</a>