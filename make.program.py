#!/usr/bin/env python3

import json

#with open("program.json") as f:    
with open("program_public.json") as f:    
    data = json.load(f)
f.closed

with open("programm.md", 'a') as programm,  open("programm2.md", 'a') as programm2, open("programm3.md", 'a') as programm3:
    programm.write("---\nlayout: page\ntitle: Programm\npermalink: /programm/\nweight: 5\nmenu: main\n---\n")
    programm2.write("---\nlayout: page\ntitle: Programm geordnet nach Raum \npermalink: /programm_pro_raum/\nweight: \nmenu: \n---\n")
    programm3.write("---\nlayout: page\ntitle: Programm auf einen Blick \npermalink: /programm_auf_einen_blick/\nweight: \nmenu: \n---\n")
    programm.write('<a href="../programm/">geordnet nach Uhrzeit</a><br />\n')
    programm.write('<a href="../programm_pro_raum/">geordnet nach Raum</a><br />\n')
    programm.write('<a href="../programm_auf_einen_blick">auf einen Blick</a><br />\n\n')
    programm2.write('<a href="../programm/">geordnet nach Uhrzeit</a><br />\n')
    programm2.write('<a href="../programm_pro_raum/">geordnet nach Raum</a><br />\n')
    programm2.write('<a href="../programm_auf_einen_blick">auf einen Blick</a><br />\n\n')
    programm3.write('<a href="../programm/">geordnet nach Uhrzeit</a><br />\n')
    programm3.write('<a href="../programm_pro_raum/">geordnet nach Raum</a><br />\n')
    programm3.write('<a href="../programm_auf_einen_blick">auf einen Blick</a><br />\n\n')

    programm.write("<table>\n")
    for clock in range(10,19):
        programm.write('<tr><td>&nbsp;</td></tr><tr><td colspan="3">' + str(clock) + ':00</td></tr><tr><td>&nbsp;</td></tr>\n')

    programm2.write("<table>\n")
    for room in ["W1", "W2", "W3", "V1", "V2", "V3", "V4"]:
        programm2.write('<tr><td>&nbsp;</td></tr><tr><td colspan="3">Raum ' + room + '</td></tr><tr><td>&nbsp;</td></tr>\n')

    programm3.write("<table>\n")

    for k,v in data.items():
        try:
            ident = v["Ident"]
            ident = k
            titel = v["Titel"][0].replace(" ","&nbsp;")
            name = v["Name"][0].replace(" ","&nbsp;")
            beginn = v["Zeit"]["Begin"]
            ende = v["Zeit"]["Ende"]
            raum = v["Raum"]
            inhalt = '\n'.join(v["Inhalt"])
            schlagworte = '\n'.join(v["Schlagworte"])
            vorwissen ='\n'.join(v["Vorwissen"])
            vorbereitung ='\n'.join(v["Vorbereitung"])
            if "Vortrag" in v["Typ"]:
                icon = '<img height = "18" src="../images/talk.svg">'
                icon2 = '<img height = "32" src="../../images/talk.svg">'
            elif "Workshop" in v["Typ"]:
                icon = '<img height = "18" src="../images/workshop.svg">'
                icon2 = '<img height = "32" src="../../images/workshop.svg">'
            elif "Lightning Talk" in v["Typ"]:
                icon = '<img height = "18" src="../images/lightning.svg">'
                icon2 = '<img height = "32" src="../../images/lightning.svg">'

        except (IndexError, KeyError):
            pass

        programm.write("<tr><td>" + raum + "</td><td>"+ icon + "</td><td><a href=\"../programm/" + ident + "\">" + titel + "</a></td><td>" + name + "</td></tr>\n")
        programm2.write("<tr><td>" + beginn + "</td><td>"+ icon + "</td><td><a href=\"../programm/" + ident + "\">" + titel + "</a></td><td>" + name + "</td></tr>\n")
        programm3.write("<td>" + icon + "</td><td><a href=\"../programm/" + ident + "\">" + ident + "</a></td>\n")

        with open("_talks/" + ident + ".md", 'a') as talk:
            talk.write("---\nlayout: talk\ntitle:\npermalink: /programm/" + ident + "/\nweight: \nmenu:\n---\n")

            try:
                talk.write("## " + titel + "\n\n")
                if beginn:
                    talk.write("### " + icon2 + " " + beginn + " bis " + ende + " in Raum " + raum + "\n\n")
                else:
                    talk.write("### " + icon2 + " " + " in Raum " + raum + "\n\n")
                talk.write("### " + name + "\n\n")
                if schlagworte:
                    talk.write("### Schlagworte\n\n")
                    talk.write(schlagworte + "\n\n")
                if inhalt:
                    talk.write("### Inhalt\n\n")
                    talk.write(inhalt + "\n\n")
                if vorwissen:
                    talk.write("### Vorwissen\n\n")
                    talk.write(vorwissen + "\n\n")
                if vorbereitung:
                    talk.write("#### Vorbereitung\n\n")
                    talk.write(vorbereitung + "\n\n")

            except KeyError:
                pass

        talk.closed

    programm.write("</table>")
    programm2.write("</table>")
    programm3.write("</table>")

programm.closed
programm2.closed
programm3.closed
