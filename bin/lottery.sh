#!/usr/bin/env bash

# Usage:
# $1 rows
# $2 seats per row

ROWS="$1"
COLUMNS="$2"

ROW=`shuf --input-range=1-$ROWS --head-count=1`
SEAT=`shuf --input-range=1-$COLUMNS --head-count=1`

# Display result
echo -e "Reihe: $ROW, Sitz: $SEAT\n"

# Draw grid
for ((row=1; row <=$ROWS; row++))
do
  for ((col=1; col <=$COLUMNS; col++))
  do
    if [[ "$col" -eq "$SEAT" && "$row" -eq "$ROW" ]]
    then
      printf x
    else
      printf -
    fi
  done
  printf "\n"
done
