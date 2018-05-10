---
layout: talk
title:
permalink: /2018/programm/christian-brauner-linux-device-management-making-the-kernel-and-udev-namespace-aware/
weight:
menu:
---
## Linux Device Management: Making the Kernel and Udev Namespace Aware

### <img height = "32" src="../../../images/talk.svg"> 11:00 bis 11:50 in Raum V2

### Christian Brauner

On non-embedded systems device management in Linux is a task split between kernelspace and userspace. Since the implementation of the devtmpfs pseudo filesystem the kernel is solely responsible for creating device nodes while udev in userspace is mainly responsible for consistent device naming and permissions. The devtmpfs filesystem however is not namespace aware. As such devices always belong to the initial user namespace. In times of SR-IOV enabled devices it is possible and needed to hand off devices to non-initial user namespaces. The last couple of months I've been working on making device management in the Kernel namespace aware. With recent patchsets of mine we have now reached that goal. As such userspace can now tie devices to a specific user namespace. This talk aims to do a couple of things. First, to give a more in-depth explanation of device management in Linux. Second, to explain the concept of namespace aware device management. Third, to explain the patchsets that were needed to make device management namespace aware. And last, to argue for a proper in-kernel solution by namespacing devtmpfs itself in the future.

### Vorwissen

I'll explain anything that's missing even if it means we can't get through everything. I can't fit all links that are helpful down below so I'll add a couple of them here:
- devtmpfs: See [https://lwn.net/Articles/331818/](https://lwn.net/Articles/331818/) for an overview and [https://lwn.net/Articles/330985/](https://lwn.net/Articles/330985/) for the actual patchset
- ueventd (Android's device manager): [https://android.googlesource.com/platform/system/core/+/master/init/ueventd.cpp](https://android.googlesource.com/platform/system/core/+/master/init/ueventd.cpp)
- systemd-udevd: [https://www.freedesktop.org/software/systemd/man/udev.html](https://www.freedesktop.org/software/systemd/man/udev.html)
- eudev (standalone fork of systemd-udevd): [https://github.com/gentoo/eudev](https://github.com/gentoo/eudev)

### Über mich

Christian Brauner is a core developer and maintainer of the LXD, LXC, and glibc projects. He works upstream for Canonical as part of the Ubuntu Server team on the Linux Kernel and lower-level problems. He's been active in the open source community for a long time and is a frequent speaker at various large Linux events; he is also strongly committed to working in the open, and a strong proponent of Free Software.

### Links

- <a href="https://patchwork.ozlabs.org/patch/906304/" target="_blank">uevent: add alloc_uevent_skb() helper</a>
- <a href="https://patchwork.ozlabs.org/patch/906302/" target="_blank">netns: restrict uevents</a>
- <a href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=94e5e3087a67c765be98592b36d8d187566478d5" target="_blank">net: add uevent socket member</a>
- <a href="https://git.kernel.org/pub/scm/linux/kernel/git/torvalds/linux.git/commit/?id=692ec06d7c92af8ca841a6367648b9b3045344fd" target="_blank">netns: send uevent messages</a>
