---
layout: talk
title:
url: /2019/programm/christian-brauner-file-descriptors-for-processes/
weight:
menu:
---
## File Descriptors For Processes

### <img height = "32" src="../../../images/talk.svg"> 14:00 bis 14:50 in Raum V1 {#-1400-bis-1450-in-raum-v1}

### Christian Brauner

Traditionally processes are identified by process identifiers aka PIDs. These are globally unique identifiers. As such users do not hold a stable reference on the process they identify. Because of that PIDs will be recycled by the kernel. This means a PID might refer to a different process than what a user thought it did. As such PIDs are inherently racy, e.g. a process might end up sending a signal to PID which referes to a process it didn't itend to signal.  
To solve this long-standing problem Jann Horn and I have introduced the concept of file descriptors for processes aka pidfds into the kernel. As things stand kernel 5.2. might gain the ability to refer to processes via file descriptors, making it possible for a process to get a stable and private reference on a process. Even if the PID is recycled the pidfd will refer to the original process.  
In this talk I will look at the history (in other systems) and the general idea of using pidfds, the work we had to do, and what we have planned for the future.

### Vorwissen

Some knowledge around process management and process identifiers (PIDs) and file descriptors (fds) would be nice. But we can work around it. :)

### Über mich

Christian Brauner is a kernel engineer and core developer and maintainer of the LXD and LXC projects. He works mostly upstream on the Linux Kernel and lower-level problems. He is strongly committed to working in the open, and a strong proponent of Free Software.

### Links

- <a href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=a9dce6679d736cb3d612af39bab9f31f8db66f9b" target="_blank">pidfd_send_signal syscall</a>
- <a href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=eac7078a0fff1e72cf2b641721e3f55ec7e5e21e" target="_blank">CLONE_PIDFD flag for clone syscall</a>
- <a href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=b53b0b9d9a613c418057f6cb921c2f40a6f78c24" target="_blank">Making pidfds pollable</a>
- <a href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=32fcb426ec001cb6d5a4a195091a8486ea77e2df" target="_blank">pidfd_open() syscall</a>