---
layout: talk
title:
permalink: /2019/programm/adrian-reber-container-live-migration/
weight:
menu:
---
## Container Live Migration

### <img height = "32" src="../../../images/talk.svg"> 17:30 bis 17:50 in Raum V1

### Adrian Reber

The difficult task to checkpoint and restore a process is used in many container runtimes to implement container live migration. This talk will give details how CRIU is able to checkpoint and restore processes, how it is integrated in different container runtimes and which optimizations CRIU offers to decrease the downtime during container migration.

In this talk I want to provide details how CRIU checkpoints and restores a process. Starting from ptrace() to pause the process, how parasite code is injected into the process to checkpoint the process from its own address space. How CRIU transforms itself to the restored process during restore. How SELinux and seccomp is restored.

I also want to give an overview how CRIU uses userfaultfd for lazy migration and dirty page tracking for pre-copy migration.

I want to end this talk with an overview about how CRIU is integrated in different container runtimes to implement container live migration.

### Über mich

Adrian is a Principal Software Engineer at Red Hat and is migrating processes at least since 2010. He started to migrate processes in a high performance computing environment and at some point he migrated so many processes that he got a PhD for that. Occasionally he still migrates single processes.

