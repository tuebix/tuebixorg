#!/usr/bin/env bash

# Usage:
# $1 rows
# $2 seats per row

set -o errexit
set -o nounset

# Asks if the user wants to continue:
ask_continue() {
  while true; do
    read -rp "Continue? [Y/n]: " answer
    if [[ "$answer" =~ ^(|[Yy](es)?|[Nn]o?)$ ]]; then
      [[ "$answer" =~ ^[Yy]|^$ ]] && retval=0
      [[ "$answer" =~ ^[Nn] ]] && retval=1
      return "$retval"
    fi
    echo "Invalid input, please try again."
  done
}

# Check the arguments:
if [[ $# -lt 1 || $# -gt 2 ]]; then
  echo "Usage: $(basename $0) ROWS [COLUMNS]"
  echo "Got $# arguments, expecting 1 or 2 arguments"
  exit 1
fi

# Parse the arguments:
declare -ri ROWS="$1"
declare -ri COLUMNS="${2:-8}"

# Variable to force unique winners (no duplicates):
declare -a winners
declare -i number_of_winners=0

# Variables to determine the current winner
declare -i row seat id

while [[ $number_of_winners -lt $(($ROWS*$COLUMNS)) ]]; do
  clear

  # Determine a new unique winner:
  while true; do
    row=`shuf --input-range=1-$ROWS --head-count=1`
    seat=`shuf --input-range=1-$COLUMNS --head-count=1`
    id=$(($row*$COLUMNS + $seat))
    if [[ ! -v winners[$id] ]]; then
      winners[$id]=1
      break
    fi
  done

  # Display the result:
  echo -e "Reihe: $row, Sitz: $seat"
  echo -e "(Von vorne links)\n"

  # Draw the grid:
  if [[ "$COLUMNS" -eq 8 ]]; then
    echo "+-+"
    echo "|x|"
    echo "+-+"
    echo ""
  fi
  for ((table_y=1; table_y <=$ROWS; table_y++))
  do
    for ((table_x=1; table_x <=$COLUMNS; table_x++))
    do
      if [[ "$table_x" -eq "$seat" && "$table_y" -eq "$row" ]]
      then
        printf x
      else
        printf -
      fi
    done
    printf "\n"
  done

  number_of_winners+=1
  ask_continue || break
done

if [[ $number_of_winners -eq $(($ROWS*$COLUMNS)) ]]; then
  echo "Maximum number of unique winners reached."
fi
