#!/usr/bin/env python3

"""A simple script to extract the talks per room for our LaTeX scripts."""
"""Usage (from the directory for the current year): ./extract-talks.py $ROOM"""

import json
import sys

if len(sys.argv) != 2:
    print("Error: Please provide a room name.", file=sys.stderr)
    print(f"Usage: {sys.argv[0]} room", file=sys.stderr)
    sys.exit(1)

room = sys.argv[1]

with open("talks.json") as talksfile:
    talks = json.load(talksfile)

talks = list(filter(lambda talk: talk["room"] == room, talks))
talks.sort(key=lambda talk: talk["timebegin"])

for talk in talks:
    print("\\talk{" + talk["timebegin"] + "}{" + talk["titel"] + "}{" + talk["name"] + "}")
