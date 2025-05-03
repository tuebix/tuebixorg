---
layout: talk
title:
url: /2015/programm/guckes-muttgpg2/
weight: 
menu:
---
## mutt + gpg - Sichere Email {#muttgpg-sichereemail}

### <img height = "32" src="../../../images/workshop.svg"> 14:00 bis 16:00 in Raum W1 {#-1400-bis-1600-in-raum-w1}

### Sven Guckes {#svenguckes}

Jeder Teilnehmer soll Mutt und GPG ausprobieren können.
Am Anfang logt sich jeder erstmal auf der lokalen Maschine ein.
Dann gehen alle per mosh/ssh auf die zentrale Kiste (Server), welche die notwendigen Programme anbietet.
Jeder generiert sich ein neues Schlüsselpaar.
Wir schauen uns den Schlüssel genauer an und laden ihn auf einen (lokalen) Testserver hoch.
(Darüber können wir Schlüssel austauschen ohne die üblichen Keyserver zu verwenden.)
Dann können wir das Auffinden von Schlüsseln ausprobieren, die Schlüssel der anderen herunterladen und diese anzeigen lassen.
Dann geht es ans Versenden von Emails - mit Signatur und/oder auch verschlüsselt.
Ein paar Anpassungen von gpg bzw mutt oder auch des Editors und der Shell können den Umgang sehr vereinfachen.
Eventuell gibt es noch eine Key Signing Party.
Diese kann über den lokalen Keyserver geschehen - oder auch bei einem eigenen Termin des Events.

### Vorwissen

- Terminal: Starten - mit einer Shell darin. (CTRL-ALT-T oder so)
- Shell: Navigieren und Editieren (Löschen und Einsetzen): CTRL-A, CTRL-E, ALT-B, ALT-F, CTRL-D CTRL-H, CTRL-W, CTRL-U (clear line), CTRL-K (kill rest of line), CTRL-T (transpose), CTRL-L (clear).
- Verwendung der history, z.B. über event designators oder per CTRL-R (reverse incremental search)
- Editor: Kenntnis einer der beiden Editoren (emacs bzw vim). Benutzer von anderen Editoren werden auch zugelassen - wenn sie keine dummen Fragen über Editoren stellen

### Vorbereitung

- den mailer mutt ("all mailers suck - but mutt sucks less")
- das "OpenPGP encryption and signing tool" GnuPG (gpg)
- die beiden Editoren (emacs+vim) (okay - evtl jed+nano)
- terminal multiplexer wie screen+tmux, sowie die shells bash und zsh
- Dann verwenden alle auch denselben Server - und können sich auch lokal emailen, z.B.:
  $ echo dies ist ein test | mutt -s test otheruser

### Links

- (Digitale) Schlüssel (Cryptokeys) <a href="http://de.wikipedia.org/wiki/Schl%C3%BCssel_(Kryptologie)" target="_blank">de.wikipedia.org/wiki/Schlüssel_(Kryptologie)</a>
- Digital Signatur <a href="http://de.wikipedia.org/wiki/Digitale_Signatur" target="_blank">de.wikipedia.org/wiki/Digitale_Signatur</a>
- Verschlüsselung <a href="http://de.wikipedia.org/wiki/Verschl%C3%BCsselung" target="_blank">de.wikipedia.org/wiki/Verschlüsselung</a>
- Schlüsselverwaltung (key management) <a href="http://en.wikipedia.org/wiki/Key_management" target="_blank">en.wikipedia.org/wiki/Key_management</a>
- Key Server - Schlüsselserver <a href="http://de.wikipedia.org/wiki/Schl%C3%BCsselserver" target="_blank">de.wikipedia.org/wiki/Schlüsselserver</a>
- KeySigning Party <a href="http://de.wikipedia.org/wiki/Keysigning-Party" target="_blank">de.wikipedia.org/wiki/Keysigning-Party</a>
- Web of Trust <a href="http://de.wikipedia.org/wiki/Web_of_Trust" target="_blank">de.wikipedia.org/wiki/Web_of_Trust</a>
- pad: <a href="https://tuebix2015.titanpad.com/guckes-muttgpg2" target="_blank">tuebix2015.titanpad.com/guckes-muttgpg2</a>
