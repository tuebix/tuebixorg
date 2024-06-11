#!/usr/bin/env python3

import json
from datetime import datetime, timedelta
import pprint


with open("schedule.json", "r") as file:
    schedule = json.load(file)

#print(schedule)

def fix_line_endings(s):
    """Replace DOS line endings with Unix line endings."""
    return s.replace("\r\n", "\n")

def merge_persons(persons):
    names = " & ".join(p['public_name'] for p in persons)
    if len(persons) == 1:
        bios = persons[0]['biography']
    else:
        bios = ""
        for p in persons:
            if not p['biography']:
                continue
            bios += "\n\n"
            bios += f"#### {p['public_name']}\n\n"
            bios += p['biography']

    if not bios:
        bios = ""

    return names, bios

def gen_talks():
    for roomname, room in schedule['schedule']['conference']['days'][0]['rooms'].items():
        for talk in room:
            answers = list(filter(lambda a: a['question'] == 1, talk['answers']))
            pre_knowledge = answers[0]['answer'] if answers else ""

            duration = datetime.strptime(talk['duration'],"%H:%M")
            delta = timedelta(hours=duration.hour, minutes=duration.minute)

            start = datetime.strptime(talk['start'], "%H:%M")
            end = start + delta

            names, bios = merge_persons(talk['persons'])

            slug = talk['slug'].removeprefix("tuebix-2024-")
            # TODO: Try to improve the URL IDs for 2025 (maybe just ID + URL
            # parameters for talk and author names (as they could change)?

            # TODO: Drop these hacks:
            if talk['id'] == 92:
                slug = "tuebix-init"
                names = "Tübix Orga Team"
            elif talk['id'] == 93:
                slug = "tuebix-exit"
                names = "Tübix Orga Team"

            yield {
                "name": names,
                "titel": talk['title'],
                "inhalt": fix_line_endings(talk['abstract']),
                "aboutme": fix_line_endings(bios),
                "vorwissen": fix_line_endings(pre_knowledge),
                "urlid": slug,
                "duration": int(delta.total_seconds() / 60),
                "room": roomname,
                "timebegin": talk['start'],
                "timeend": end.strftime("%H:%M"),
                "weblinks": {}
            }

pp = pprint.PrettyPrinter(indent=4)

talks = list(gen_talks())

pp.pprint(talks)

with open("talks.json", "w") as outfile:
    json.dump(talks, outfile, indent=4)
