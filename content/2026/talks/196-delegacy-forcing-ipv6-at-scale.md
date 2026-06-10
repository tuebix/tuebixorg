---
layout: talk
title:
url: /2026/programm/196-delegacy-forcing-ipv6-at-scale/
weight:
menu:
---
## DeLegacy: Forcing IPv6 at Scale

### <img height = "32" src="../../../images/talk.svg"> 13:00 bis 13:50 in Raum V5 (C215)

### Mynacol

#### Abstract

Find out how to increase the proportion of IPv6 traffic by manipulating DNS responses, and how to persuade X/Twitter and Discord to support IPv6 _(caveats apply)_.

#### Beschreibung

Content Delivery Networks (CDNs) generate significant traffic, and almost all of them support IPv6. However, many websites that use CDNs lack IPv6 support. But when accessed over the right IPv6 address, these websites work without issue. With targeted DNS manipulations, the number of domains with IPv6 can be increased significantly. I have developed the [DeLegacy RPZ](https://codeberg.org/IPv6-Monostack/delegacy-rpz) project to achieve this.  
This talk explains the underlying mechanisms and how they can be utilized for this purpose. It shows how standard DNS servers, such as BIND or Unbound, can be configured to perform this task instead of using custom code. I reveal how to use DNS [Response Policy Zones](https://wikipedia.org/wiki/Response_policy_zone), [DNAMEs](https://de.wikipedia.org/wiki/DNAME_Resource_Record), and [DNS64](https://datatracker.ietf.org/doc/rfc6147/) to implement the intended manipulations. I also present my approach to identifying and testing useful domains and IP addresses when creating new rules. Finally, I present statistics on the increased IPv6 penetration, based on the [Tranco list](https://tranco-list.eu/).

### Über mich

Hacker with passions for self hosting, security, privacy, NixOS and IPv6. Find me on the [Fediverse](https://social.mynacol.xyz/mynacol).

