#!/usr/bin/env python3

import json
import sys
import io

def parse_weblink(weblinks):
    link_list = []
    for val in weblinks.values():
        title = val['title']
        url = val['url']
        if not title:
            title = url
        link_list.append('- <link href="' + url + '">' + title + '</link>')
    return "\n".join(link_list)


def giggitytimes(minutes): 
    hour = minutes // 60
    minutes = minutes % 60
    return "%02d:%02d" % (hour, minutes) 


with io.open('talks.json', 'r', encoding='utf8') as talksfile:
    data = json.load(talksfile)

with io.open('giggity.xml', 'w', encoding='utf8') as gigxml:
    gigxml.write('<?xml version="1.0"?>\n<schedule>\n<conference>\n<title>Tübix 2019</title>\n<city>T&#xFC;bingen</city>\n<start>2019-07-06</start>\n<end>2019-07-06</end>\n<days>1</days>\n<release>1.20190531.1112</release>\n<timeslot_duration>00:30</timeslot_duration>\n</conference>\n<day date="2019-07-06" index="1">\n')

# TODO Teleskop, Bienen, LPIC, generic helper slots
    for roomsection in ['V1', 'V2', 'V3', 'V4', 'W1', 'W2']:
        gigxml.write('<room name="' + roomsection + '">\n')
        for talk in data:
            if talk["room"] == roomsection:
                gigxml.write('<event id="' + talk["urlid"] + '">\n')
                gigxml.write('<start>' + talk['timebegin'] + '</start>\n')
                gigxml.write('<duration>' + giggitytimes(talk['duration']) + '</duration>\n')
                gigxml.write('<room>' + talk['room'] + '</room>\n')
                gigxml.write('<title>' + talk['titel'] + '</title>\n')
                gigxml.write('<description>' + talk['inhalt'] + '\n')
                if talk['aboutme']:
                    gigxml.write('\n#### Über mich\n\n')
                    gigxml.write(talk['aboutme'] + '\n')
                if talk['vorwissen']:
                    gigxml.write('\n#### Vorwissen\n\n')
                    gigxml.write(talk['vorwissen'] + '\n')
                gigxml.write('</description>\n')
                gigxml.write('<persons><person>' + talk['name'] + '</person></persons>\n')
                if talk["weblinks"]:
                    gigxml.write("<links>\n")
                    gigxml.write(parse_weblink(talk["weblinks"]))
                    gigxml.write("\n</links>\n")
                gigxml.write('</event>\n\n')
        gigxml.write('</room>\n')
    gigxml.write('</day>\n</schedule>')
