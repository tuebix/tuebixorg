---
layout: talk
title:
permalink: /2016/programm/michael-weiss-keysigning-party/
weight:
menu:
---
## OpenPGP Key-Signing-Party (aka. Fingerprint Exchange) im Anschluss an den GnuPG Workshop

### <img height = "32" src="../../../images/workshop.svg"> 16:00 bis 17:00 in Raum V3

### Sven Guckes, Florian Heimgärtner, Michael Weiss

### Vorbereitung

Man sollte seinen eigenen Fingerprint in ausgedruckter Form mitbringen!
Am besten bringt man noch eine Schreibunterlage mit, damit man sich besser
Notizen auf die eigene Liste machen kann ;)

Wir empfehlen den Besuch des Workshops 14-16h im Raum W3:
[E-Mail-Verschlüsselung mittels GnuPG und das Web of Trust](../michael-weiss-e-mail-verschluesselung-mittels-gnupg-und-das-web-of-trust)

### Ablauf

Wir bitten alle Teilnehmer rechtzeitig zu erscheinen, da wir die zu druckende
Liste nur anhand der tatsächlich vorhandenen Leute erstellen werden.

* Aufnahme aller Teilnehmer und ihrer Schlüssel-IDs (dabei evtl. schon die
  Fingerprints checken).
* Abschluss der Liste. Danach keine weiteren Aufnahmen mehr!
* Herunterladen aller teilnehmenden Schlüssel vom Keyserver.
* Aufbereitung der Liste mit gpgparticipants (Paket signing-party).
* Ausdrucken der Liste.
* Verteilung der Liste an alle Teilnehmer.
    * Diese sollte nun nicht mehr unbeaufsichtigt weggelegt werden!
* Teilnehmer nach Listennummer aufstellen.
* Erklärung des defaults:
    * Schlüssel unterschreiben und hochladen.
    * Wer mag, kann die unterschriebenen Schlüssel gerne an die Leute mailen
      (Infos zu caff findet man unten).
* Jeder liest seinen Fingerprint vor.
    * Laut ,deutlich und nicht zu schnell reden.
    * Wenn man sich verspricht am besten nochmal den aktuellen Block (4 Zeichen)
      wiederholen.
* Häkchen setzen nur dann, wenn man der Information  soweit vertraut, dass man
  den Schlüssel auch unterschreiben will.
* Es werden anhand der Listennummern zwei gleichlange Reihen gebildet.
* Eine Reihe überprüft die Identitäten, die andere Reihe zeigt ihre Ausweise.
    * Man rotiert so lange bis man wieder dem ursprünglichen Partner begegnet.
    * Man kann statt Häkchen auch einfach Zahlen (z. B. von 0-3 verwenden wie
      sicher man die Identität überprüft hat).
* Nach der KSP sollte man die Liste sicher verwahren (am besten gleich
  zusammengefaltet in den Geldbeutel oder so)!

### Nachbearbeitung

Das Signieren der Schlüssel erfolgt dann zuhause.

Da während der KSP nur die Identitäten überprüft werden, jedoch nicht die
E-Mail-Adressen würde es sich anbieten das Tool
[caff](https://pgp-tools.alioth.debian.org/) ("CA fire and forget" aus dem Paket
signing-party) zu verwenden.

Zur Konfiguration ruft man am besten einmal `caff` von der Kommandozeile auf und
überprüft dann die erstellte Datei "~/.caffrc".

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

# My account (posteo.de example, with pass as password manager)
account max
  host posteo.de
  from max.mustermann@posteo.de
  user max.mustermann@posteo.de
  passwordeval "pass posteopasswortfile"

# Set the default account
account default : john
```

Anschließend setzt man noch mittels `chmod 600 ~/.msmtprc` die korrekten
Zugriffsrechte (msmtp beschwert sich auch wenn man dies vergisst).

Nachdem man nun caff konfiguriert hat kann man über die Kommandozeile mittels
`caff <key>` die entsprechenden Keys signieren (Achtung: Die Fingerprints
sollten natürlich mit denen auf der Liste verglichen werden!).

### Kontakt

| Name                 | E-Mail                        | OpenPGP-Key (Creation date)                                                                                                                |
| :------------------- | :---------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------- |
| Sven    Guckes       | <tuebix2016@guckes.net>       | [rsa8000/0xEAB97F200185391B](https://sks-keyservers.net/pks/lookup?op=vindex&search=0xEAB97F200185391B&fingerprint=on&exact=on) 2014-03-11 |
| Florian Heimgaertner | <florian@heimgaertner.net>    | [rsa4096/0x975D004EEF4515A5](https://sks-keyservers.net/pks/lookup?op=vindex&search=0x975D004EEF4515A5&fingerprint=on&exact=on) 2015-06-13 |
| Michael Weiss        | <michael.weiss1996@gmail.com> | [rsa4096/0x1E8B02C29318BA46](https://sks-keyservers.net/pks/lookup?op=vindex&search=0x1E8B02C29318BA46&fingerprint=on&exact=on) 2015-10-08 |

### Links

- GnuPG: <a href="https://www.gnupg.org/" target="_blank">https://www.gnupg.org/</a>
- OpenPGP: <a href="https://tools.ietf.org/html/rfc4880" target="_blank">https://tools.ietf.org/html/rfc4880</a>
