#!/usr/bin/env python3

import json
from datetime import datetime, timedelta
import pprint


with open("schedule.json", "r") as file:
    schedule = json.load(file)

#print(schedule)

def merge_persons(persons):
    names = " & ".join(p['public_name'] for p in persons)
    bios = "\n\n".join(p['biography'] for p in persons)

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

            slug = talk['slug'].lstrip("tuebix-2023-")

            if talk['id'] == 76:
                slug = "tuebix-init"
                names = "Tübix Orga Team"
            elif talk['id'] == 77:
                slug = "tuebix-exit"
                names = "Tübix Orga Team"
                
            yield {
                "name": names,
                "titel": talk['title'],
                "inhalt": talk['abstract'],
                "aboutme": bios,
                "vorwissen": pre_knowledge,
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