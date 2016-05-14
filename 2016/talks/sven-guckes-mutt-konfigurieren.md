---
layout: talk
title:
permalink: /2016/programm/sven-guckes-mutt-konfigurieren/
weight:
menu:
---
## mutt konfigurieren

### <img height = "32" src="../../../images/workshop.svg"> 10:00 bis 12:00 in Raum V3

### Sven Guckes

= Abstract =

Mutt Config: "den mutt mailer einstellen"

Wir werden die Konfigurationsdatei (~/.muttrc) editieren,
und eventuell in mehrere Dateien aufteilen
(mit dem Kommando "source" verbinden.)
Zunächst die schnellen Änderungen,
dann die längeren Themen angehen.

# Voraussetzungen

* laptop - installiert mit mutt + $EDITOR (emacs,vim)
* mutt-1.5.23 (debian), neueste version: mutt-1.6.1 [2016-04-30]
* mutt schonmal verwendet, besser: in Verwendung.
* editor - sicherer umgang damit: Dateien öffnen,
  schnelles Suchen, ändern der Inhalte, speichern.
* plus: gewohnter Umgang mit der Shell.
* plus: gewohnter Umgang mit "screen" oder "tmux".

### Inhalt 

# Schnelle Änderungen

* autoedit + edit_headers
* reverse_alias + reverse_name
* index_format + to_chars
* header      (Auswahl, Reihenfolge, Farben)
* attachments (Auswahl, mailcap processing)
* Farben für den Header und den Index
* signatures (vim: register; ":r ~/.sig.foo")

# Längere Themen

* mailinglisten: folder_hook, mailboxes, subscribe, save_hook
* farben: für den message body
* display_filter: Änderungen und Löschungen mit "sed"
* macros: limits, header weeding, change personality
* pgp_commands: Signieren, Verschlüsseln
* retrieval: Mails holen per fetchmail und sortieren mit procmail
* imap: TODO

# Vorbereitung

Eventuell wird es keinen Zugang zum Internet geben.
Wir müssen also vorbereitet sein.

Ich bitte alle Teilnehmer darum einen Laptop mitzunehmen und
auf diesem schon vorher ein Paket von mutt zu installieren.

Das Versenden von Email muss dann eventuell
über das eigene Handy per Tethering geschehen:
<a href="https://de.wikipedia.org/wiki/Tethering" target="_blank">https://de.wikipedia.org/wiki/Tethering</a>

Ich werde diese Datei lokal zur Verfügung stellen.
Aber natürlich ist es besser, sie schon vorher runterzuladen.

Falls es Fragen gibt, so bitte ich Euch
diese mir schon vorab per Email zu schicken.

Während des Workshop verwenden wir dieses Pad:
<a href="https://tuebix2016.titanpad.com/workshop-mutt" target="_blank" https://tuebix2016.titanpad.com/workshop-mutt</a>

Falls es keinen Zugang zum Internet gibt, dann werde
ich auf meiner Kiste zeigen, was mit mutt moeglich ist.
Das Senden und Empfangen von Emails wird dann nicht gehen.
Fuer den Fall hoffe ich, dass ihr eure eigenen Daten
auf der Kiste habt und darauf operieren könnt.

### Links

- <a href="http://www.guckes.net/tuebix2016/workshop.mutt_config.txt" target="_blank">http://www.guckes.net/tuebix2016/workshop.mutt_config.txt</a>
