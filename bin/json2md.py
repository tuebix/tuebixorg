#!/usr/bin/env python3

"""
Usage: ./json2md.py
Converts a JSON document containing all CfP submissions for the Tübix to Markdown files
Requires: "talks.json" in the current directory (from orig2talks.py)
Creates: A directory "talks" with all talks and a file "programm2.md" in the current directory
"""

import json
import sys
import os
import re
import urllib.parse

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
    prog2.write("---\nlayout: page\ntitle: Programm\npermalink: /2019/programmentwurf/\nweight:\nmenu:\n---\n\n<table>\n")


for talk in data:
    # TODO: Ignore these pages for now:
    ignored_urlids = [
            "alexander-landstorfer-das-tuebinger-80cm-teleskop"
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
            mdf.write("---\nlayout: talk\ntitle:\npermalink: /2019/programm/" + talk["urlid"] + "/\nweight:\nmenu:\n---\n")
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
                else:
                    mdf.write('talk.svg')
                cssclass = "talk"
            mdf.write('"> ' + talk["timebegin"] + " bis " + talk["timeend"] + " in Raum " + talk["room"] + "\n\n")
            mdf.write("### " + talk["name"] + "\n\n")

            mdf.write(transform_linefeeds(talk["inhalt"]) + "\n\n")
            if talk["vorwissen"]:
                mdf.write("### Vorwissen\n\n" + transform_linefeeds(talk["vorwissen"]) + "\n\n")
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
