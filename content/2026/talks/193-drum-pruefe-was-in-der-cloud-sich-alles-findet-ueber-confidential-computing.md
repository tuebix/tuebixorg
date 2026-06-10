---
layout: talk
title:
url: /2026/programm/193-drum-pruefe-was-in-der-cloud-sich-alles-findet-ueber-confidential-computing/
weight:
menu:
---
## „"Drum pruefe was in der Cloud sich alles findet" Ueber Confidential-Computing“

### <img height = "32" src="../../../images/talk.svg"> 11:00 bis 11:50 in Raum V4 (C118a)

### Uli Kleemann

#### Abstract

Confidential Computing: Warum der Schutz Ihrer Daten in der Cloud erst im Arbeitsspeicher  
beginnt  
Die unsichtbare Lücke: Warum verschlüsselte Daten in der Cloud trotzdem angreifbar sind  
Die Cloud ist heute das Rückgrat der digitalen Wirtschaft. Doch selbst wenn Daten verschlüsselt  
gespeichert und übertragen werden, bleibt eine kritische Schwachstelle: der Arbeitsspeicher. Während  
der Verarbeitung – also genau dann, wenn Daten entschlüsselt und genutzt werden – liegen sie im  
Klartext im RAM. Angreifer können diese Phase ausnutzen, etwa durch Cold-Boot-Angriffe, bei  
denen der Arbeitsspeicher physisch oder über Schwachstellen ausgelesen wird. Selbst moderne  
Verschlüsselung schützt hier nicht. Die Folge: Sensible Daten wie Kundeninformationen,  
Geschäftsgeheimnisse oder medizinische Datensätze sind im entscheidenden Moment ungeschützt.  
Das Problem: Traditionelle Verschlüsselung endet dort, wo die Daten tatsächlich genutzt werden – und  
genau dort beginnt das Risiko.  
TEE: Vertrauenswürdige Enklaven für maximale Sicherheit  
Trusted Execution Environments (TEE) sind die Antwort auf dieses Dilemma. Ein TEE ist ein  
geschützter Bereich im Prozessor, der Daten und Anwendungen isoliert von anderen Prozessen – selbst  
vom Cloud-Anbieter oder Hypervisor – verarbeitet. Nur autorisierte Anwendungen können auf die  
Daten im TEE zugreifen, und selbst der Systemadministrator hat keinen Zugriff.  
Wie funktioniert das?  
• Hardware-basierte Isolierung: Der Prozessor selbst schafft eine „Enklave“, in der Daten  
verschlüsselt bleiben – auch während der Verarbeitung.  
• Kein Zugriff von außen: Selbst wenn ein Angreifer den Server kompromittiert, kann er die  
Daten im TEE nicht auslesen.  
• Vertrauenskette: Nur authentifizierte und autorisierte Code-Teile dürfen in der Enklave  
ausgeführt werden.  
Praktische Konsequenz: TEEs schließen die Lücke zwischen „Daten in Ruhe“ (verschlüsselt  
gespeichert) und „Daten in Nutzung“ (entschlüsselt im RAM).  
Confidential Computing: Der nächste Schritt für sichere Cloud-Anwendungen  
Confidential Computing geht noch einen Schritt weiter: Es kombiniert TEEs mit verschlüsselten  
Datenströmen und sicheren Ausführungsumgebungen, um Daten während der gesamten  
Verarbeitung zu schützen – nicht nur bei der Speicherung oder Übertragung.  
Die Vorteile für Unternehmen:  
• Schutz vor Insider-Bedrohungen: Selbst Cloud-Administratoren oder staatliche Akteure  
können nicht auf die Daten zugreifen.  
• Compliance und Datenschutz: Sensible Daten (z. B. nach DSGVO, HIPAA oder KritisV)
bleiben auch in der Cloud geschützt.  
• Vertrauen in Multi-Cloud-Szenarien: Unternehmen können Daten sicher zwischen  
verschiedenen Cloud-Anbietern verarbeiten, ohne das Risiko von Datenlecks.  
• Zukunftssicherheit: Confidential Computing ist die Grundlage für sichere KI, Blockchain und  
vertrauliche Datenanalysen in der Cloud.  
Beispiel: Ein Gesundheitsunternehmen kann Patientendaten in der Cloud analysieren, ohne dass der  
Cloud-Anbieter oder Dritte Zugriff auf die Rohdaten erhalten.  
Warum jetzt handeln? Die Bedrohung ist real – die Lösung ist verfügbar  
Cold-Boot-Angriffe und andere Methoden zum Auslesen des Arbeitsspeichers sind keine theoretischen  
Szenarien. Studien zeigen, dass Angreifer gezielt diese Schwachstelle ausnutzen, um an sensible Daten  
zu gelangen. Gleichzeitig bieten alle großen Cloud-Anbieter (AWS, Azure, Google Cloud) bereits  
Confidential-Computing-Lösungen an – oft als einfache Erweiterung bestehender Dienste.  
Die Frage ist nicht mehr, ob Sie Confidential Computing brauchen, sondern wann Sie es  
einführen.  
• Für KMU: Schutz von Kunden- und Geschäftsgeheimnissen ohne teure Infrastruktur.  
• Für Konzerne: Compliance und Sicherheit für globale Datenströme.  
• Für alle: Ein entscheidender Schritt, um das Vertrauen in die Cloud zu stärken.  
Fazit: Vertrauen ist gut, hardwarebasierte Isolierung ist besser  
Confidential Computing und TEEs lösen ein zentrales Problem der Cloud-Sicherheit: den Schutz von  
Daten während der Verarbeitung. Wer heute sensible Daten in der Cloud nutzt, sollte diese  
Technologien nicht als Option, sondern als Notwendigkeit betrachten. Die Alternative – das Risiko  
von Datenlecks, Compliance-Verstößen und Vertrauensverlust – ist schlicht nicht akzeptabel.  
Denken Sie daran: In der Cloud sind Ihre Daten nur so sicher wie ihre schwächste Phase – und das ist  
nicht die Speicherung, sondern die Nutzung.  
Diskussionsfrage: Welche Daten oder Anwendungen in Ihrem Unternehmen wären durch Confidential  
Computing besonders geschützt – und welche Risiken könnten Sie damit konkret minimieren?

### Über mich

Linux-Admin  CISO und Auditor fuer ISO 27001

https://udapro.de

