#!/usr/bin/env python3

import json
import sys


def parse_weblink(weblinks):

    link_list = []
    for val in weblinks.values():
        title = val['title']
        url = val['url']

        if not title:
            title = url

        link_list.append('- <a href="' + url + '" target="_blank">' + title + '</a>')

    return "\n".join(link_list)




with open("talks.json") as talksfile:
    data = json.load(talksfile)

with open('programm2.md', 'w') as prog2:
    prog2.write("---\nlayout: page\ntitle: Programm\npermalink: /2017/programmentwurf/\nweight:\nmenu:\n---\n\n<table>\n")


for talk in data:
    with open('talks/' + talk["urlid"] + '.md', 'w') as mdf, open('programm2.md', 'a') as prog2:
        try:
            mdf.write("---\nlayout: talk\ntitle:\npermalink: /2017/programm/" + talk["urlid"] + "/\nweight:\nmenu:\n---\n")
            mdf.write("## " + talk["titel"] + "\n\n")
            mdf.write('### <img height = "32" src="../../../images/')
            if talk["duration"] == 120:
                mdf.write('workshop.svg')
                cssclass = "work"
            elif talk["duration"] == 5:
                mdf.write('lightning.svg')
                cssclass = "light"
            else:
                mdf.write('talk.svg')
                cssclass = "talk"
            mdf.write('"> ' + talk["timebegin"] + " bis " + talk["timeend"] + " in Raum " + talk["room"] + "\n\n")
            mdf.write("### " + talk["name"] + "\n\n")

            mdf.write(talk["inhalt"] + "\n\n")
            if talk["vorwissen"]:
                mdf.write("### Vorwissen\n\n" + talk["vorwissen"] + "\n\n")
            if talk["aboutme"]:
                mdf.write("### Über mich\n\n")
                mdf.write(talk["aboutme"]+ "\n\n")
            if talk["weblinks"]:
                mdf.write("### Links\n\n")
                mdf.write(parse_weblink(talk["weblinks"]))



            #print('<td rowspan="4"><a class="', cssclass, '"><a href="../programm/', talk["urlid"], '">', talk["titel"].replace(' ','&nbsp;'), '</a></td>', file=prog1, sep='')
            print('<tr><td>', talk["timebegin"], '</td><td><a class="', cssclass, '"></a></td><td><a href="../programm/', talk["urlid"], '">', talk["titel"].replace(' ','&nbsp;'), '</a></td><td>', talk["name"].replace(' ', '&nbsp;'),'</td></tr>', file=prog2, sep='')

        except AttributeError as e1:
            raise e1.with_traceback()



        except:
            e = sys.exc_info()[0]
            print(talk["titel"])
            print(e)

            #prog1.write('"><a href="../programm/' + talk["urlid"] + '" target="_blank">' + talk["titel"] + '</a>\n')
            #<td rowspan="4"><a class="work" href="../programm/mundt_nachbauer-jessie_party">Jessie&nbsp;Party</a></td>

            # raumplan / zeitplan


with open('programm2.md', 'a') as prog1:
    prog1.write("</table>")
