#!/usr/bin/env python3

"""
Usage: ./convert_from_pretalx.py [YEAR]
Creates: "talks.json" based on the JSON data from our Pretalx CfP server.
"""

import json
import sys
from datetime import datetime, timedelta
import urllib.request
import os


YEAR = int(sys.argv[1] if len(sys.argv) == 2 else datetime.now().year)
if YEAR != 2025:
    print("Warning: Potentially unsupported year.")

schedule_url = f"https://cfp.tuebix.org/tuebix-{YEAR}/schedule/export/schedule.json"
with urllib.request.urlopen(schedule_url) as data:
    schedule = json.load(data)
with open("schedule.json", "w") as file:
    json.dump(schedule, file)

# TODO: Don't hardcode the year, answer IDs, etc.
answers_url = f"https://cfp.tuebix.org/api/events/tuebix-{YEAR}/answers/?question=5&limit=100"
req = urllib.request.Request(answers_url)
req.add_header('Authorization', f'Token {os.environ["TUEBIX_PRETALX_TOKEN"]}')
with urllib.request.urlopen(req) as data:
    all_answers = json.load(data)["results"]
with open("answers.json", "w") as file:
    json.dump(all_answers, file)

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
                pre_knowledge_answer = list(filter(lambda a: a["question"] == 5, talk_answers))
                if pre_knowledge_answer:
                    assert(len(pre_knowledge_answer) == 1)
                    pre_knowledge = pre_knowledge_answer[0]["answer"]

            duration = datetime.strptime(talk['duration'],"%H:%M")
            delta = timedelta(hours=duration.hour, minutes=duration.minute)

            start = datetime.strptime(talk['start'], "%H:%M")
            end = start + delta

            names, bios = merge_persons(talk['persons'])

            slug = talk['slug'].removeprefix(f"tuebix-{YEAR}-")
            # TODO: Try to improve the URL IDs for 2025 (maybe just ID + URL
            # parameters for talk and author names (as they could change)?

            # TODO: Drop these hacks:
            if talk['id'] == 160:
                slug = "tuebix-init"
                names = "Tübix Orga Team"
            elif talk['id'] == 161:
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
