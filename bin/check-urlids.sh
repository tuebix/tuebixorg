#!/usr/bin/env bash

# Checks all URL IDs (urlid field) in talks.json for special characters
# Whitelist: a-z A-Z and "-" (but not "--")
# TODO: Remove this script and figure out a proper URL ID solution for automatic
# imports from Pretalx.

echo "Potentially problematic URL IDs:"
grep urlid talks.json | sed -E 's/ +"urlid": "(.*)",/\1/' | \
  grep -E --color=always '[^a-zA-Z0-9-]|--' # | less -R
