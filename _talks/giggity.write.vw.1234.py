#!/usr/bin/env python3

from sys import argv
import re
from pprint import pprint

p1 = re.compile('.*/programm/(.*)-(.*)/')
p2 = re.compile('^##\s+(.*)')
p3 = re.compile('^###\s+<img.+?src="../../images/(.+?).svg"> (\d\d:\d\d) bis (\d\d:\d\d) in (.+)')
p4 = re.compile('^###\s+(.*)')

h = {}

idspeaker = ""
idtitle   = ""
type = ""
title = ""
start = ""
room = ""
persons = ""

with open (argv[1], "r") as talkfile:
    for line in talkfile:

        m1 = p1.match(line)
        if m1:
            idspeaker = m1.group(1)
            idtitle   = m1.group(2)
            h["id"] = idspeaker + "-" + idtitle

        m2 = p2.match(line)
        if m2:
            title = m2.group(1)
            #h["title"] = title.replace("&nbsp;", " ").replace("&","und")
            h["title"] = title.replace("&nbsp;", " ")

        m3 = p3.match(line)
        if m3:
            type  = m3.group(1) 
            start = m3.group(2) 
            end   = m3.group(3) 
            room  = m3.group(4) 
            h["type"] = type 
            h["start"] = start 
            if "Raum" in room:
                h["room"] = room.replace("Raum ","")
            else:
                h["room"] = room 

        m4 = p4.match(line)
        if m4:
            persons  = m4.group(1) 
            if idspeaker in persons.lower().replace("ä",'ae').replace("ö",'oe').replace("ü",'ue'):
                h["persons"] = persons.replace("&nbsp;", " ").replace(",","und")
            else:
                pass
        
roomname = room.lower().split(" ")[1]

with open (roomname, "a") as outfile:
    outfile.write('<event id="' + h["id"] +'">\n')
    try:
        outfile.write('<start>' + h['start'] + '</start>\n')
    except KeyError:
        print("keyerror: " + h["id"])

    if h["id"] in ["gottschall-teleskop", "seidel-tcp_stealth", "reber-mirrorserver", "behrla-lpic", "hofmann-surfen", "uebele-bitcoin", "weissensel-fish", "genannt-sshkey_distribution", "kuestner-strohmaier-wueste_welle", "klaeren-computermuseum", "imme-latex_verein", "hofmann-lug_berlin"]:
        outfile.write('<duration>' + '00:30' + '</duration>\n')
    elif h["id"] in ["blechschmidt-haskell","willbold-python_kinder_buch","stadelmeier_wannenmacher-tor_router","blechschmidt-sandstorm","helmle-einfache_sprache","koelbel-desktop_auth","giesen-seafile","widmayer-nagerit","franke-ruby","humm-wikipedia","schiebel-oss_schule","willbold-python_kinder_buch","stadelmeier_wannenmacher-tor_router","blechschmidt-sandstorm","helmle-einfache_sprache","koelbel-desktop_auth","giesen-seafile","widmayer-nagerit","franke-ruby","humm-wikipedia","schiebel-oss_schule"]:
        outfile.write('<duration>' + '00:10' + '</duration>\n')
    elif type == "workshop":
        outfile.write('<duration>' + '02:00' + '</duration>\n')
    elif type == "talk":
        outfile.write('<duration>' + '01:00' + '</duration>\n')

    outfile.write('<room>' + h['room'] + '</room>\n')
    outfile.write('<title>' + h['title'] + '</title>\n')
    outfile.write('<type>' + h['type'] + '</type>\n')
    outfile.write('<description>' + "description" + '</description>\n')
    try:
        outfile.write('<persons><person id="' + idspeaker + '">' + h['persons'] + '</person></persons>\n')
    except KeyError:
        outfile.write('<persons><person id="' + idspeaker + '">' + "xxx" + '</person></persons>\n')
        print(idspeaker)
    outfile.write('</event>\n')

