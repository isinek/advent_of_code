#!/bin/bash

## Usage: advent_of_code.sh [-d day] [-t task]
##     -d day  - day has values 1-25
##     -t task - task has values 1 or 2
## For other info check: https://adventofcode.com/
##

#######################################
# Print help text.
# Arguments:
#   None
#######################################
function print_help() {
  local find_re="^## "

  sed -n "/${find_re}/p" "$0" | sed -E "s/${find_re}(.+)/\1/"
}

#######################################
# MAIN
#######################################

declare -i days
mapfile days < <( seq 1 25 )

declare -i tasks=( 1 2 )
declare -A input_files=(
  ["1_1"]=day1.in ["1_2"]=day1.in
  ["2_1"]=day2.in ["2_2"]=day2.in
  ["3_1"]=day3.in ["3_2"]=day3.in
)

while getopts 'd:t:' arg; do
  case "${arg}" in
    d) days=( "${OPTARG}" ) ;;
    t) tasks=( "${OPTARG}" ) ;;
    *) exit 1 ;;
  esac
done

for d in "${days[@]}"; do
  for t in "${tasks[@]}"; do
    if [ -z "${input_files[${d}_${t}]}" ]; then
      continue
    elif [ ! -r "day${d}_task${t}.sh" ]; then
      echo "Solution for day ${d} and task ${t} does not exist!"
      exit 2
    elif [ ! -r "${input_files[${d}_${t}]}" ]; then
      echo "Input file for day ${d} and task ${t} does not exist!"
      exit 2
    fi

    solution=$( bash "day${d}_task${t}.sh" "${input_files[${d}_${t}]}" )
    echo "Day ${d} task ${t} solution: ${solution}"
  done
done
