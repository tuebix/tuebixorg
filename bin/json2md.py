#!/usr/bin/env python3

"""
Usage: ./json2md.py [YEAR]
Converts a JSON document containing all CfP submissions for the Tübix to Markdown files
Requires: "talks.json" in the current directory (from orig2talks.py)
Creates: A directory "talks" with all talks and a file "programm2.md" in the current directory
"""

import json
import sys
import os
import re
import urllib.parse

from textwrap import dedent
from datetime import datetime

# Optional: Determine if the program should be added to the main menu, and add
# the other Markdown files.

YEAR = int(sys.argv[1] if len(sys.argv) == 2 else datetime.now().year)

def parse_weblink(weblinks):

    link_list = []
    for val in weblinks.values():
        title = val['title']
        url = val['url']

        if not title:
            title = url

        link_list.append('- <a href="' + url + '" target="_blank">' + title + '</a>')

    return "\n".join(link_list)

def room_to_sort_key(room):
    # Order: Workshops -> Talks -> other stuff
    if room.startswith("W"):
        priority = "0"
    elif room.startswith("V"):
        priority = "1"
    else:
        priority = "2"
    return priority + room

with open("talks.json") as talksfile:
    data = json.load(talksfile)
    data.sort(key=lambda talk: room_to_sort_key(talk["room"]) + talk["timebegin"])

with open('programm2.md', 'w') as prog2:
    prog2.write(f"---\nlayout: page\ntitle: Programm\npermalink: /{YEAR}/programm/\nweight:\nmenu: main\n---\n\n")
    prog2.write(dedent("""\
      * <span style="font-weight: bold;">Programm</span>
      * <a href="../programm_rahmen/">Rahmenprogramm</a>
      * <a href="../lageplan/">Lageplan</a>
      * <a href="../programm_was_bedeuten_die_icons">Was bedeuten die Icons <img height="18" width="18" src="../../images/workshop.svg"> <img height="18" width="18" src="../../images/talk.svg"> <img height="18" width="18" src="../../images/talk2.svg"> <img height="18" width="18" src="../../images/lightning.svg"> ?</a>

      **Hinweis:** Weitere Infos zum Kinderprogramm folgen noch.

    """))
    prog2.write("Alternativ kann das Program auch über Pretalx angesehen werden: ")
    prog2.write(f"[cfp.tuebix.org/tuebix-{YEAR}/schedule/](https://cfp.tuebix.org/tuebix-{YEAR}/schedule/)\n\n")
    giggity_link = f"https://ggt.gaa.st/#url=https://cfp.tuebix.org/tuebix-{YEAR}/schedule/export/schedule.xml"
    prog2.write(f"Unter Android kann man folgenden Link verwenden um das Programm in die App [Giggity](https://github.com/Wilm0r/giggity) zu laden: [{giggity_link}]({giggity_link})\n\n")
    prog2.write("<table>\n")

visited_rooms = []
for talk in data:
    # TODO: Ignore these pages for now:
    ignored_urlids = [
            "alexander-landstorfer-das-tuebinger-80cm-teleskop",
            "matthias-windrich-imkern-als-hobby"
    ]
    if talk["urlid"] in ignored_urlids:
        continue
    # TODO: Change the format for the URL ID? E.g. "name_title" instead of "name-title"?:
    # Old schema: thomas-rauch-das-tuebinger-80cm-teleskop
    # Possible new schema: URL encode and e.g. "+" or "_" between the name and title?
    def transform_linefeeds(string):
        # Remove leading and trailing "\n" (optional normalization):
        string = re.sub(r'^\n+|\n+$', '', string)
        # Replace " *\n" with "  \n" but keep "\n\n" (two spaces cause a line break):
        string = re.sub(r'([^(\n)]) *\n([^(\n)])', r'\1  \n\2', string)
        # Note: Replacing "\n" with "<br/>" would be nicer but doesn't work for lists.
        return string
    def normalize_string(string):
        # TODO: The current implementation is probably not consistent with 2015-2018
        string = string.replace("/", "")
        string = string.replace("ä", "ae").replace("ö", "oe").replace("ü", "ue")
        string = string.replace("Ä", "Ae").replace("Ö", "Oe").replace("Ü", "Ue")
        string = re.sub(r"[^- A-Za-z0-9]+", '', string) # Whitelist (TODO: Very restrictive!)
        normalized = re.sub(" +", "-", string.lower().replace("-", ""))
        # Optional:
        #urllib.parse.quote(normalized, safe="") # Only as additional precaution
        return normalized
    urlid = normalize_string(talk["name"]) + "_" + normalize_string(talk["titel"])
    os.makedirs("talks", exist_ok=True)
    with open('talks/' + talk["urlid"] + '.md', 'w') as mdf, open('programm2.md', 'a') as prog2:
        try:
            mdf.write(f"---\nlayout: talk\ntitle:\npermalink: /{YEAR}/programm/" + talk["urlid"] + "/\nweight:\nmenu:\n---\n")
            mdf.write("## " + talk["titel"] + "\n\n")
            mdf.write('### <img height = "32" src="../../../images/')
            if talk["duration"] == 110:
                mdf.write('workshop.svg')
                cssclass = "work"
            elif talk["duration"] == 5:
                mdf.write('lightning.svg')
                cssclass = "light"
            else:
                if talk["urlid"] in [ "tuebix-exit", "tuebix-init" ]:
                    mdf.write('talk2.svg')
                    cssclass = "talk2"
                else:
                    mdf.write('talk.svg')
                    cssclass = "talk"
            mdf.write('"> ' + talk["timebegin"] + " bis " + talk["timeend"] + " in Raum " + talk["room"] + "\n\n")
            mdf.write("### " + talk["name"] + "\n\n")

            mdf.write("#### Abstract\n\n")
            mdf.write(transform_linefeeds(talk["abstract"]) + "\n\n")

            if talk["description"]:
                mdf.write("#### Beschreibung\n\n")
                mdf.write(transform_linefeeds(talk["description"]) + "\n\n")

            if talk["vorwissen"]:
                mdf.write("#### Vorwissen\n\n" + transform_linefeeds(talk["vorwissen"]) + "\n\n")
            if talk["aboutme"]:
                if re.search("\+|,", talk["name"]): # One or multiple speakers?
                    mdf.write("### Über uns\n\n")
                else:
                    mdf.write("### Über mich\n\n")
                mdf.write(transform_linefeeds(talk["aboutme"])+ "\n\n")
            if talk["weblinks"]:
                mdf.write("### Links\n\n")
                mdf.write(parse_weblink(talk["weblinks"]))



            #print('<td rowspan="4"><a class="', cssclass, '"><a href="../programm/', talk["urlid"], '">', talk["titel"].replace(' ','&nbsp;'), '</a></td>', file=prog1, sep='')
            if talk["room"] not in visited_rooms:
                if len(visited_rooms) > 0:
                    prog2.write("<tr><td>&nbsp;</td></tr>\n")
                prog2.write("<tr><td></td><td></td><td></td><td></td><td>Raum " + talk["room"] + "</td></tr>\n")
                visited_rooms.append(talk["room"])
            if not "urlidnew" in talk:
                print('<tr><td>', talk["timebegin"], '</td><td>bis</td><td>', talk["timeend"], '</td><td><a class="', cssclass, '"></a></td><td><a href="../programm/', talk["urlid"], '">', talk["titel"].replace(' ','&nbsp;'), '</a></td><td>', talk["name"].replace(' ', '&nbsp;'),'</td></tr>', file=prog2, sep='')

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
    prog1.write("</table>\n")
