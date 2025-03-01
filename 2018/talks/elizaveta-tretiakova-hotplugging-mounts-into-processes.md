---
layout: talk
title:
url: /2018/programm/elizaveta-tretiakova-hotplugging-mounts-into-processes/
weight:
menu:
---
## Hotplugging Mounts Into Processes

### <img height = "32" src="../../../images/talk.svg"> 17:00 bis 17:50 in Raum V2 {#-1700-bis-1750-in-raum-v2}

### Elizaveta Tretiakova

Being able to dynamically interact with mounts while a container is running has been a long-standing request from many container users. The idea is to dynamically add mounts to a container without polluting the host's mount namespace. An example would be adding a new dedicated storage device to the container before it runs out of disk space. Interacting with mounts at container runtime is also necessary in order to add new devices to containers. Over the last couple of months I have worked on implementing mount hotplug as part of my bachelor thesis into LXC containers. To this end I wrote a new API function "mount" that users can call to inject mounts into a running container. In this talk I will explain how this all works and how I've implemented this functionality.

### Links

- <a href="https://github.com/lxc/lxc/pull/2300" target="_blank">Mount Injection Pull Request</a>
- <a href="https://www.kernel.org/doc/Documentation/filesystems/sharedsubtree.txt" target="_blank">Mount Propagation</a>