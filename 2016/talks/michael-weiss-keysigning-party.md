---
layout: talk
title:
permalink: /2016/programm/michael-weiss-keysigning-party/
weight:
menu:
---
## PGP Key-Signing-Party im Anschluss an den GnuPG Workshop

### <img height = "32" src="../../../images/workshop.svg"> 16:00 bis 17:00 in Raum V3

### Sven Guckes, Florian Heimgärtner, Michael Weiss

### Vorbereitung 

Wir empfehlen den Besuch des Workshops 14-16h im Raum W3:
[E-Mail-Verschlüsselung mittels GnuPG und das Web of Trust](../michael-weiss-e-mail-verschluesselung-mittels-gnupg-und-das-web-of-trust)

### Ablauf

Wir bitten alle Teilnehmer rechtzeitig zu erscheinen,
da wir die zu druckende Liste nur anhand der
tatsächlich vorhandenen Leute erstellen werden.

* Aufnahme aller Teilnehmer und ihrer Schlüssel-IDs (dabei evtl schon die fingerprints checken.)
* Abschluß der Liste. Keine weiteren Aufnahmen.
* Herunterladen aller teilnehmenden Schlüssel vom Keyserver.
* Aufbereitung der Liste mit Software (Paket signing-party)
* Ausdrucken der Liste.
* Verteilung der Liste an alle Teilnehmer.
* Leute nach Listennummer aufstellen.
* Erklärung des defaults:
    * Schlüssel unterschreiben und hochladen.
    * Wer mag, kann die unterschriebenen Schlüssel gerne an die Leute mailen.
* Jeder liest seinen Fingerprint nochmal vor.
    * Laut reden, deutlich reden.
    * ABCDEF: ALPHA BRAVO CHARLIE DELTA ECHO FOXTROT <https://en.wikipedia.org/wiki/NATO_phonetic_alphabet>
* "Häkchen setzen nur dann, wenn man der Information  soweit vertraut, dass man es auch unterschreiben will."

Dann das übliche aneinander-vorbeilaufen.  aber:
Nur *eine* Seite checkt IDs - die anderen *zeigen* ihre IDs.


### Nachbearbeitung 

Das Signieren der Schlüssel erfolgt dann zuhause.

Da während der KSP nur die Identitäten überprüft werden, jedoch nicht die
E-Mail-Adressen würde es sich anbieten das Tool
[caff](https://pgp-tools.alioth.debian.org/) ("CA fire and forget" aus dem Paket
signing-party) zu verwenden. Zur Konfiguration ruft man am besten einmal `caff`
von der Kommandozeile auf und überprüft dann die erstellte Datei "~/.caffrc".
Damit caff Mails versenden kann braucht man noch einen MTA. Dazu installiert man
sich am besten einfach msmtp-mta (msmtp mit sendmail alias) und legt die Datei
"~/.msmtprc" mit folgendem Inhalt an:

```
# Set default values for all following accounts.
defaults
  port 587
  auth on
  tls on
  tls_starttls on
  tls_trust_file /etc/ssl/certs/ca-certificates.crt
  tls_certcheck on
  logfile ~/.msmtp.log

# My account (GMail example)
account john
  host smtp.gmail.com
  from john.doe@gmail.com
  user john.doe@gmail.com
  password MyPassword
  #passwordeval "cat ~/some-file"

# Set the default account
account default : john
```

Anschließend setzt man noch mittels `chmod 600 ~/.msmtprc` die korrekten
Zugriffsrechte (msmtp beschwert sich auch wenn man dies vergisst).

Nachdem man nun caff konfiguriert hat kann man über die Kommandozeile mittels
`caff <key>` die entsprechenden Keys signieren (Achtung: Die Fingerprints
sollten natürlich mit denen auf der Liste verglichen werden!).

### Kontakt 

* Sven      Guckes       <tuebix2016@guckes.net>        8000R/0185391B 2014-03-11
* Florian   Heimgaertner <florian@heimgaertner.net>     4096R/EF4515A5 2015-06-13
* Michael   Weiss        <michael.weiss1996@gmail.com>  4096R/9318BA46 2015-10-08



### Links

- GnuPG: <a href="https://www.gnupg.org/" target="_blank">https://www.gnupg.org/</a>
- OpenPGP: <a href="https://tools.ietf.org/html/rfc4880" target="_blank">https://tools.ietf.org/html/rfc4880</a>
