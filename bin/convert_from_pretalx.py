#!/usr/bin/env python3

import json
from datetime import datetime, timedelta
import urllib.request


schedule_url = "https://cfp.tuebix.org/tuebix-2024/schedule/export/schedule.json"
with urllib.request.urlopen(schedule_url) as data:
    schedule = json.load(data)
with open("schedule.json", "w") as file:
    json.dump(schedule, file)

# TODO: Don't hardcode the year, answer IDs, etc.
answers_url = "https://cfp.tuebix.org/api/events/tuebix-2024/answers/?format=json&limit=100"
with urllib.request.urlopen(answers_url) as data:
    all_answers = json.load(data)["results"]

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
            # answers = list(filter(lambda a: a['question'] == 1, talk['answers']))
            # pre_knowledge = answers[0]['answer'] if answers else ""

            submission = talk["url"].split("/")[5]
            talk_answers = list(filter(lambda a: a["submission"] == submission, all_answers))
            pre_knowledge = ""
            if talk_answers:
                pre_knowledge_answer = list(filter(lambda a: a["question"]["id"] == 4, talk_answers))
                if pre_knowledge_answer:
                    assert(len(pre_knowledge_answer) == 1)
                    pre_knowledge = pre_knowledge_answer[0]["answer"]

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
                "abstract": fix_line_endings(talk['abstract']),
                "description": fix_line_endings(talk['description']),
                "aboutme": fix_line_endings(bios),
                "vorwissen": fix_line_endings(pre_knowledge),
                "urlid": slug,
                "duration": int(delta.total_seconds() / 60),
                "room": roomname,
                "timebegin": talk['start'],
                "timeend": end.strftime("%H:%M"),
                "weblinks": {}
            }

talks = list(gen_talks())

with open("talks.json", "w") as outfile:
    json.dump(talks, outfile, indent=4)
