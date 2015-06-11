---
layout: page
title: asciinema
permalink: /asciinema/
weight: 
menu: 
---

<script type="text/javascript" src="https://asciinema.org/a/17654.js" id="asciicast-17654" async></script>

Der Vorteil hierbei ist, dass die Dateien im Vergleich zu Videos sehr klein sind und die Kommandos abkopiert (statt abgetippt) werden können.

### Installation

Am besten NICHT über den Paketmanager installieren, sondern hier das neuste Release herunterladen:<br/>
<a href="https://github.com/asciinema/asciinema/releases/latest" target="_blank">github.com/asciinema/asciinema/releases/latest</a><br/>
Die Executables sind statisch gelinkt, d.h. es sind keine weiteren Bibliotheken nötig.<br/>
Herunterladen, Auspacken und Starten (siehe unten)<br/>
Am besten schonmal zu Hause vorher testen...<br/>

### Tipp, um automatischen Upload zu vermeiden

asciinema will standardmäßig die Aufnahme hochladen auf asciinema.org. <br/>
Um das zu verhindern kann als Argument einen Dateiname übergeben werden,<br/>
in den die Aufnahme abgespeichert wird: <br/>
./asciinema rec meine.aufnahme.01 <br/>
 <br/>
Wiedergabe mit: <br/>
./asciinema play meine.aufnahme.01
