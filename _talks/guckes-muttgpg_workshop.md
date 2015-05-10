---
layout: talk
title:
permalink: /programm/guckes-muttgpg_workshop/
weight: 
menu:
---
## mutt+gpg&nbsp;-&nbsp;Sichere&nbsp;Email

### <img height = "32" src="../../images/workshop.svg"> 14:00 bis 16:00 in Raum W1

### Sven&nbsp;Guckes

### Schlagworte

(Digitale) Schlüssel (Cryptokeys)
http://de.wikipedia.org/wiki/Schl%C3%BCssel_(Kryptologie)
Digital Signatur
http://de.wikipedia.org/wiki/Digitale_Signatur
Verschlüsselung
http://de.wikipedia.org/wiki/Verschl%C3%BCsselung
Schlüsselverwaltung (key management)
http://en.wikipedia.org/wiki/Key_management
Key Server - Schlüsselserver
http://de.wikipedia.org/wiki/Schl%C3%BCsselserver
KeySigning Party
http://de.wikipedia.org/wiki/Keysigning-Party
Web of Trust
http://de.wikipedia.org/wiki/Web_of_Trust

### Inhalt

Jeder Teilnehmer soll Mutt und GPG ausprobieren können.
Am Anfang logt sich jeder erstmal auf der lokalen Maschine ein.
Dann gehen alle per mosh/ssh auf die zentrale Kiste (Server),
welche die notwendigen Programme anbietet.
Jeder generiert sich ein neues Schlüsselpaar.
Wir schauen uns den Schlüssel genauer an und
laden ihn auf einen (lokalen) Testserver hoch.
(Darüber können wir Schlüssel austauschen
ohne die üblichen Keyserver zu verwenden.)
Dann können wir das Auffinden von Schlüsseln
ausprobieren, die Schlüssel der anderen
herunterladen und diese anzeigen lassen.
Dann geht es ans Versenden von Emails -
mit Signatur und/oder auch verschlüsselt.
Ein paar Anpassungen von gpg bzw mutt
oder auch des Editors und der Shell
können den Umgang sehr vereinfachen.
Eventuell gibt es noch eine Key Signing Party.
Diese kann über den lokalen Keyserver geschehen -
oder auch bei einem eigenen Termin des Events.

### Vorwissen

terminal:   Starten - mit einer Shell darin. (ctrl-alt-t oder so)
shell:      Navigieren und Editieren (Löschen und Einsetzen).
CTRL-A CTRL-E, ALT-B ALT-F, CTRL-D CTRL-H, CTRL-W;
CTRL-U (clear line), CTRL-K (kill rest of line),
CTRL-T (transpose), CTRL-L (clear).
verwendung der history, zB über event designators
oder per CTRL-R (reverse incremental search)
editor:     Kenntnis einer der beiden Editoren (emacs bzw vim).
Benutzer von anderen Editoren werden auch zugelassen -
wenn sie keine dummen Fragen über Editoren stellen.

#### Vorbereitung

== Server ==
den mailer mutt (all mailers suck - but mutt sucks less).
das "OpenPGP encryption and signing tool" GnuPG (gpg),
die beiden Editoren (emacs+vim) (okay - evtl jed+nano),
terminal multiplexer wie screen+tmux, sowie die shells bash+zsh.
Dann verwenden alle auch denselben Server -
und können sich auch lokal emailen, zB:
$ echo dies ist ein test | mutt -s test otheruser
== Netz+Raum ==
* Ein Raum mit PCs und Linux (egal welcher geschmackrichtung).
* Logins auf jedem Rechner - oder einem zentralen Server.
* Ports offen für ssh (22) und mosh (60000-61000) - und
zum Keyserver (11371).  Am besten gar kein Port Filtering.
* Verbindungen per Kabel+WLAN für eigene Rechner (laptop+notebooks).

