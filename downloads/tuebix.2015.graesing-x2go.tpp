## Diese Präsentation wurde mit Hilfe von VIM erstellt und kann
## mit dem Programm TPP http://www.ngolde.de/tpp.html wiedergegeben werden
## 

--author Heinz-M. Graesing, Mihai Moldovan, Stefan Krug
--title X2Go Workshop Tübingen
--date today
--huge X2Go
--boldon
Wilkommen zum X2Go Workshop @ Tübix.
--boldoff
--color cyan 
Lösungen und Probleme für das Thema Remote Computing
--color white 

 o o
  ϒ  ΞX2Go



--newpage agenda_1
--heading Agenda
--color cyan
--boldon
  * Was wird benötigt?
--boldoff
  * Erste Installation von X2GoClient
  * Verbindung zum Demo Server
  * Theorie
    - Was ist X2go
    - Woraus besteht X2Go
    - Welche Probleme erzeut ein Remote Desktop
  * Praxis
    - Erste Installation X2GoServer
    - Erste Konfiguration X2GoClient
    - Erweiterter Konfiguration X2GoClient
    - Erweteiterte Konfiguration X2GoServer
  * Bei Zeitüberfluss
    - Betrieb einer Thin Client Umgebung
    - Gedanken zu einer Multinode Installation
       + Datenhaltung
       + Load Balancing
       + X2GoBroker
--color white
  * Fragen




--newpage requirements
--heading Was wird benötigt?
  * Internet
  * Terminal
    - Erfahrungen mit SCREEN
    - Erfahrungen mit VIM
    - Erfahrungen mit SSH
  * X2GoClient
  * Installationsziel (X2GoServer)
    - LXC Container (Debian JESSIE ohne SSYSTEMD)
    - Virtuelle Maschine (Debian JESSIE ohne SSYSTEMD)
  * Geduld




--newpage agenda_2
--heading Agenda
--color cyan
  * Was wird benötigt?
--boldon
  * Erste Installation von X2GoClient
--boldoff
  * Verbindung zum Demo Server
  * Theorie
    - Was ist X2go
    - Woraus besteht X2Go
    - Welche Probleme erzeut ein Remote Desktop
  * Praxis
    - Erste Installation X2GoServer
    - Erste Konfiguration X2GoClient
    - Erweiterter Konfiguration X2GoClient
    - Erweteiterte Konfiguration X2GoServer
  * Bei Zeitüberfluss
    - Betrieb einer Thin Client Umgebung
    - Gedanken zu einer Multinode Installation
       + Datenhaltung
       + Load Balancing
       + X2GoBroker
--color white
  * Fragen




--newpage x2goclient_first_installation_1
--heading Erste Installation X2GoClient

--center Ist X2GoClient bereits Teil meiner Distribution?
---

X2GoClient in den Paketquellen suchen:
--beginshelloutput
$ apt-cache search x2goclient
x2goclient - X2Go Client application (Qt4)
x2goclient-dbg - X2Go Client application (Qt4), debug symbols (client)
--endshelloutput

---

X2GoClient ist bereits in den Quellen von
   * Debian Wheezy/Jessie
   * Ubuntu >12.04
   * und anderen Distributionen
enthalten.

---

X2GoServer NICHT!





--newpage x2goclient_first_installation_2
--heading Erste Installation X2GoClient

Falls X2GoClient nicht über die Paketquellen angeboten wird, kann er durch 
Hinzufügen der offiziellen X2Go Paket Repositories installiert werden:

--- 

Schlüssel des X2Go Repositories hinzufügen:
--beginshelloutput
$ apt-key adv --recv-keys --keyserver keys.gnupg.net E1F958385BFE2B6E
--endshelloutput

---

X2Go Repository Quellen hinzufügen: 
--beginshelloutput
$ vi /etc/apt/sources.list.d/x2go.list
--endshelloutput

Inhalt der Datei /etc/apt/sources.list.d/x2go.list:
--beginoutput
# X2Go Repository (release builds)
deb http://packages.x2go.org/debian jessie main
# X2Go Repository (sources of release builds)
deb-src http://packages.x2go.org/debian jessie main

# X2Go Repository (nightly builds)
#deb http://packages.x2go.org/debian jessie heuler
# X2Go Repository (sources of nightly builds)
#deb-src http://packages.x2go.org/debian jessie heuler
--endoutput

---

--color cyan 
Download URL: http://wiki.x2go.org/doku.php/doc:installation:start
--color white




--newpage x2goclient_first_installation_3
--heading Erste Installation X2GoClient

X2Go Keyring installieren: 
--beginshelloutput
$ apt update
$ apt install x2go-keyring
$ apt update
--endshelloutput

---

X2GoClient installieren: 
--beginshelloutput
$ apt install x2goclient
--endshelloutput




--newpage agenda_3
--heading Agenda
--color cyan
  * Was wird benötigt?
  * Erste Installation von X2GoClient
--boldon
  * Verbindung zum Demo Server 
--boldoff
  * Theorie
    - Was ist X2go
    - Woraus besteht X2Go
    - Welche Probleme erzeut ein Remote Desktop
  * Praxis
    - Erste Installation X2GoServer
    - Erste Konfiguration X2GoClient
    - Erweiterter Konfiguration X2GoClient
    - Erweteiterte Konfiguration X2GoServer
  * Bei Zeitüberfluss
    - Betrieb einer Thin Client Umgebung
    - Gedanken zu einer Multinode Installation
       + Datenhaltung
       + Load Balancing
       + X2GoBroker
--color white
  * Fragen




--newpage requirements
--heading Verbindung zum Demo Server

---

Zugangsdaten Workshop Demo Server
--color cyan 
--beginoutput
Host:        ****
Login:       ****
SSH-Port:    22
Sitzungsart: "Zugriff auf lokalen Desktop"
--endoutput




--newpage agenda_4
--heading Agenda
--color cyan
  * Was wird benötigt?
  * Erste Installation von X2GoClient
  * Verbindung zum Demo Server 
--boldon
  * Theorie
    - Was ist X2go
    - Woraus besteht X2Go
    - Welche Probleme erzeut ein Remote Desktop
--boldoff
  * Praxis
    - Erste Installation X2GoServer
    - Erste Konfiguration X2GoClient
    - Erweiterter Konfiguration X2GoClient
    - Erweteiterte Konfiguration X2GoServer
  * Bei Zeitüberfluss
    - Betrieb einer Thin Client Umgebung
    - Gedanken zu einer Multinode Installation
       + Datenhaltung
       + Load Balancing
       + X2GoBroker
--color white
  * Fragen




--newpage theorie_was_ist_X2Go
--heading Was ist X2Go?

  * Was kann X2Go?
  * Was kann X2Go NICHT?
  * Wer steckt hinter X2Go?




--newpage theorie_woraus_besteht_x2go
--heading Woraus besteht X2Go?

  * Ein Blick in die Pakete
  * Abhängigkeiten
  * Dienste
  * Initiales Debugging




--newpage theorie_welche_probleme
--heading Welche Probleme erzeut ein Remote Desktop?
  * Protokoll- / Datenübertragung
  * Umleitung Bildschirm (1,2,…;Auflösung,…)
  * Umleitung Eingabegeräte
  * Umleitung Datenträger
  * Umleitung Drucker
  * Umleitung “Warum nicht einfach ALLES”?
  * Benutzerrechte
  * Systemressourcen
  * Codecverfügbarkeit
  * Ideologie




--newpage agenda_5
--heading Agenda
--color cyan
  * Was wird benötigt?
  * Erste Installation von X2GoClient
  * Verbindung zum Demo Server 
  * Theorie
    - Was ist X2go
    - Woraus besteht X2Go
    - Welche Probleme erzeut ein Remote Desktop
--boldon
  * Praxis
    - Erste Installation X2GoServer
    - Erste Konfiguration X2GoClient
    - Erweiterter Konfiguration X2GoClient
    - Erweteiterte Konfiguration X2GoServer
--boldoff
  * Bei Zeitüberfluss
    - Betrieb einer Thin Client Umgebung
    - Gedanken zu einer Multinode Installation
       + Datenhaltung
       + Load Balancing
       + X2GoBroker
--color white
  * Fragen




--newpage praxis_installation_x2goserver_1
--heading Erste Installation X2GoServer

--color cyan
Auf dem Server
--color white

---

Schlüssel des X2Go Repositories hinzufügen:
--beginoutput
$ apt-key adv --recv-keys --keyserver keys.gnupg.net E1F958385BFE2B6E
--endoutput

X2Go Repository Quellen hinzufügen: 
--beginoutput
$ vi /etc/apt/sources.list.d/x2go.list
--endoutput

Inhalt der Datei /etc/apt/sources.list.d/x2go.list:
--beginoutput
# X2Go Repository (release builds)
deb http://packages.x2go.org/debian jessie main
# X2Go Repository (sources of release builds)
deb-src http://packages.x2go.org/debian jessie main

# X2Go Repository (nightly builds)
#deb http://packages.x2go.org/debian jessie heuler
# X2Go Repository (sources of nightly builds)
#deb-src http://packages.x2go.org/debian jessie heuler
--endoutput




--newpage praxis_installation_x2goserver_2
--heading Erste Installation X2GoServer

X2Go Keyring installieren: 
--beginoutput
$ apt update
$ apt install x2go-keyring
$ apt update
--endoutput

---

X2GoServer installieren: 
--beginshelloutput
$ apt install x2goserver x2goserver-xsession
--endshelloutput

---

Passende X2GoBindings finden: 
--beginshelloutput
$ apt search x2go bindings
x2golxdebindings - LXDE bindings for X2Go
x2gomatebindings - X2Go MATE bindings and MIME types
x2goserver-fmbindings - Generic (freedesktop-based) file manager bindings for X2Go
--endshelloutput

---

X2GoBindings installieren (am Beispiel Mate): 
--beginshelloutput
$ apt install x2gomatebindings
--endshelloutput




--newpage praxis_installation_x2goserver_2
--heading Erste Installation X2GoServer

Wo ist der Server? 
--beginshelloutput
$ ps axjf
/usr/bin/perl /usr/sbin/x2gocleansessions
/usr/lib/nx/../x2go/bin/x2goagent -extension XFIXES -nolisten tcp -nolisten tcp -dpi 96 -D -auth /home/trainer/
/bin/bash /usr/bin/x2goruncommand 50 7819 trainer-50-123_stDMATE_dp24 30002 mate-session nosnd D
 \_ mate-session
     \_ /usr/bin/mate-settings-daemon
     \_ marco
     \_ mate-panel
     |   \_ mate-terminal
     |       \_ gnome-pty-helper
     |       \_ bash
     \_ caja
     ...
--endshelloutput

---

Wer ist verbunden? 
--beginshelloutput
$ x2golistsessions_root
123|user1-*DKDE_dp24|display|server|zustand|start||client|||stop|user||
124|user2-*DKDE_dp24|display|server|zustand|start||client|||stop|user||
125|user3-*DKDE_dp24|display|server|zustand|start||client|||stop|user||
--endshelloutput



--newpage praxis_installation_x2goserver_3
--heading Erste Installation X2GoServer

Wichtige Berechtigungen? 
--beginshelloutput
$ more /etc/group |grep x2go
x2gouser:x:115:trainer
x2goprint:x:126:
x2godesktopsharing:x:128:
x2gobroker:x:129:
--endshelloutput

---

--beginshelloutput
$ x2godbadmin --help
Usage:
x2godbadmin --createdb
x2godbadmin --listusers
x2godbadmin --adduser|rmuser <UNIX user>
x2godbadmin --addgroup|rmgroup <UNIX group>
--endshelloutput




--newpage praxis_konfiguration_x2goclient_1
--heading Erste Konfiguration X2GoClient

  * Wahl des Desktops
  * Wahl einer beliebigen Anwendung
  * Wahl einer freigegebenen Anwendung
  * Verbindung über andere Protokolle
    - RDP
    - XDMCP
  * Anhalten und Fortführen von Sitzungen
  * Einschränkungen
  * “Automatische Anmeldung”
    - Schlüsselmanagement




--newpage praxis_konfiguration_x2goclient_2
--heading Erweiterter Konfiguration X2GoClient

--color yellow
GEEKTIPP:
X2GoSitzungsmanagement über Konsole!
--color white


Wie sehe ich meine Sitzung?
--beginshelloutput
$ x2golistsessions
123|user-*DKDE_dp24|display|server|zustand|start||client|||stop|user||
--endshelloutput

---

Kann ich sie auch über die Kommandozeile anhalten?
--beginshelloutput
$ x2gosuspend-session user-*KDE_dp24
--endshelloutput

---

Welche Befehle stehen noch zur Verfügung?
--beginoutput
x2goagent                     x2goresume-desktopsharing
x2gobasepath                  x2goresume-session
x2gocmdexitmessage            x2goruncommand
x2godesktopsharing            x2goserver-run-extensions
x2gofeature                   x2gosessionlimit
x2gofeaturelist               x2gosetkeyboard
x2gofm                        x2gostartagent
x2gogetapps                   x2gosuspend-desktopsharing
x2gogetservers                x2gosuspend-session
x2golistdesktops              x2goterminate-desktopsharing
x2golistmounts                x2goterminate-session
x2golistsessions              x2goumount_session
x2gomountdirs                 x2goumount-session
x2gopath                      x2goversion
x2goprint
--endoutput




--newpage praxis_konfiguration_x2goclient_3
--heading Erweiterter Konfiguration X2GoClient

  * Wahl des Desktops
  * Display
    - Packalgorithmen und Bildformate
    - Vollbild vs. Fenstermodus
  * Eingabe
    - Tastaturlayouts (Debugging)
  * Sound
    - Architekturen
  * Debugging
  * Drucker- & Dateifreigabe
    - SSHFS
    - FUSE
  * Kommandozeilenoptionen




--newpage praxis_konfiguration_x2goclient_4
--heading Erweiterter Konfiguration X2GoClient

X2GoClient Kommandozeilenoptionen
--beginshelloutput
$ x2goclient --help
Usage: x2goclient [Options]
Options:
...
--debug				 enables extensive output for console output.
--no-menu			 hide menu bar
--no-session-edit		 not allow user to edit preconfigured
				 sessions
--maximize			 start maximized
--hide				 start hidden
--portable			 start in "portable" mode
--xinerama			 use Xinerama by default
--thinclient			 run without window manager
--haltbt			 show shutdown button
--add-to-known-hosts		 add RSA key fingerprint to .ssh/known_hosts
				 if authenticity of server can't be established
--ldap=<host:port:dn> 		 start with LDAP support. Example:
				 --ldap=ldapserver:389:o=organization,c=de
...
--endshelloutput




--newpage praxis_konfiguration_x2goclient_5
--heading Erweiterter Konfiguration X2GoClient

X2GoClient Kommandozeilenoptionen
--beginoutput
...
--ldap=<host:port:dn> 		 start with LDAP support. Example:
				 --ldap=ldapserver:389:o=organization,c=de
--ssh-port=<port>		 connect to this port, default 22
--client-ssh-port=<port>	 local ssh port (for fs export), default 22
--session=<session>		 Start session 'session'
--user=<username>		 select user 'username'
--link=<modem|isdn|adsl|wan|lan>	 set default link type, default 'adsl'
--pack=<packmethod>		 set default pack method, default '16m-jpeg-9'
--clipboard=<both|client|server|none>	 set default clipboard mode, default 'both'
--kbd-layout=<layout>		 set default keyboard layout or layouts
				 comma separated
--kbd-type=<typed>		 set default keyboard type
--home=<dir>			 set users home directory
--session-conf=<file>		 path to alternative session config
--tray-icon			 force to show session trayicon
--close-disconnect		 close X2Go Client after disconnect
--hide-foldersharing			 hide all folder sharing related options
--endoutput

---

--color yellow
GEEKTIPP:
X2GoClient mit eigenem Hintergrundbild aufrufen:
--beginshelloutput
$ x2goclient --background=/pfad/zu/einem/svg
--endshelloutput
--color white



--newpage praxis_konfiguration_x2goserver_1
--heading Erweiterte Konfiguration X2GoServer

  * Absicherung des Servers
  * Auswahl an freigegebenen Programmen
  * X2GoSessionsDB (postgres)
  * Mehrfachanmeldungen erlauben / Verhindern
  * Sessions aufräumen / IDLE-Time beschränken
  * Multiserver Konzepte




--newpage praxis_konfiguration_x2goserver_2
--heading Erweiterte Konfiguration X2GoServer

X2Go Konfigurationsdateien
--beginshelloutput
$ ls /etc/x2go
applications
keystrokes.cfg
rgb
x2goagent
keyboard
x2goagent.options
x2go_logout  x2go_logout.d  x2goserver.conf  x2gosql  x2gothinclient_settings  x2gothinclient_settings_wheezy  Xresources  Xsession  Xsession.d  Xsession.options
--endshelloutput



--newpage praxis_konfiguration_x2goserver_3
--heading Erweiterte Konfiguration X2GoServer

X2Go Konfigurationsdateien
--beginshelloutput
$ vim /etc/x2go/x2goserver.conf
--endshelloutput

---

--beginoutput
$ more /etc/x2go/x2goserver.conf
[limit users]
#user-foo=1

[limit groups]
#bar-group=1

[security]
# SSHFS umask for client-side folder sharing. Leave uncommented to keep the server's default umask
#umask="0117"

[log]
# possible levels are: emerg, alert, crit, err, warning, notice, info, debug
loglevel=notice
--endoutput

---

--color red
Finger WEG!
--beginshelloutput
$ vim /etc/x2go/x2goagent.options
--endshelloutput
--color white




--newpage agenda_6
--heading Agenda
--color cyan
  * Was wird benötigt?
  * Erste Installation von X2GoClient
  * Verbindung zum Demo Server 
  * Theorie
    - Was ist X2go
    - Woraus besteht X2Go
    - Welche Probleme erzeut ein Remote Desktop
  * Praxis
    - Erste Installation X2GoServer
    - Erste Konfiguration X2GoClient
    - Erweiterter Konfiguration X2GoClient
    - Erweteiterte Konfiguration X2GoServer
--boldon
  * Bei Zeitüberfluss
    - Betrieb einer Thin Client Umgebung
    - Gedanken zu einer Multinode Installation
       + Datenhaltung
       + Load Balancing
       + X2GoBroker
--boldoff
--color white
  * Fragen




--newpage erweiterungen_x2go_1
--heading Betrieb einer Thin Client Umgebung

X2GoThinClientEnvironment
--beginshelloutput
$ apt install x2gothinclientmanagement
$ vim /etc/x2go/x2gothinclient_settings
$ x2gothinclient_create
$ x2gothinclient_preptftpboot
...
--endshelloutput

---

--color cyan
http://wiki.x2go.org/doku.php/wiki:advanced:tce:install?s[]=tce
--color white





--newpage erweiterungen_x2go_2
--heading Gedanken zu einer Multinode Installation

Wohin mit den Sitzungsdaten?
--beginshelloutput
$ more/etc/x2go/x2gosql/sql
#postgres or sqlite
backend=postgres

[postgres]
host=localhost
port=5432
...
--endshelloutput

---

--color cyan
http://wiki.x2go.org/doku.php/wiki:advanced:multi-node:x2goserver-pgsql?s[]=postgres
--color white




--newpage erweiterungen_x2go_3
--heading Gedanken zu einer Multinode Installation

Wohin mit den Serverdaten?

MultiNode über LDAP
--beginshelloutput
$ shelldap
ou=Servers,ou=ON,~ > ls
cn=server1
cn=server2
...
--endshelloutput

---

MultiNode über Broker
--beginshelloutput
$ apt search x2gobroker
python-x2gobroker - X2Go http(s) based session broker (Python modules)
x2gobroker - X2Go http(s) based session broker (executable)
x2gobroker-agent - X2Go http(s) based session broker (common files)
x2gobroker-authservice - X2Go http(s) based session broker (PAM authentication service)
x2gobroker-daemon - X2Go http(s) based session broker (daemon)
x2gobroker-wsgi - X2Go http(s) based session broker (CGI)
...
--endshelloutput

---

--color cyan
http://wiki.x2go.org/doku.php/doc:installation:x2gobroker?s[]=broker
--color white




--newpage agenda_6
--heading Agenda
--color cyan
  * Was wird benötigt?
  * Erste Installation von X2GoClient
  * Verbindung zum Demo Server 
  * Theorie
    - Was ist X2go
    - Woraus besteht X2Go
    - Welche Probleme erzeut ein Remote Desktop
  * Praxis
    - Erste Installation X2GoServer
    - Erste Konfiguration X2GoClient
    - Erweiterter Konfiguration X2GoClient
    - Erweteiterte Konfiguration X2GoServer
  * Bei Zeitüberfluss
    - Betrieb einer Thin Client Umgebung
    - Gedanken zu einer Multinode Installation
       + Datenhaltung
       + Load Balancing
--color white
--boldon
  * Fragen
--boldoff




--newpage fragen_x2go
--heading Fragen zum Workshop und X2Go
  * Was ist mit IOS?
  * Was ist mit Android?
  * Was ist mit HTML5?
  * Was ist mit IPV6?
  * Was ist mit Wayland?
  * Wie kann ich helfen?

--boldon
  * Ihre Fragen
--boldoff





--newpage ende
--heading Wir bedanken uns!
--huge Vielen Dank!

  * Heinz-M. Graesing
  * Mihai Moldovan
  * Stefan Krug

