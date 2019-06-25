#!/usr/bin/env bash

set -o errexit

if [[ ! -d ../bin ]]; then
  EXEC_DIR=$(dirname $0)/../$(date +%Y)
  cd "$EXEC_DIR"
fi

../bin/json2md.py
../bin/json2giggity.py
