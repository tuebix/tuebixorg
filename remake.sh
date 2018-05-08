#!/usr/bin/env bash

set -o errexit

./cleanup.sh
./make.program.py
jekyll serve
