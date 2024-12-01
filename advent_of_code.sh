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

  sed -n "/${find_re}/p" $0 | sed -E "s/${find_re}(.+)/\1/"
}

#######################################
# MAIN
#######################################

declare -i day=( $( seq 1 25 ) )
declare -i task=( 1 2 )

while getopts 'd:t:' arg; do
  case "${arg}" in
    d) day=(${OPTARG}) ;;
    t) task=(${OPTARG}) ;;
  esac
done

for d in ${day[*]}; do
  for t in ${task[*]}; do
    if [ ! -r day${d}_task${t}.sh ]; then
      echo "Solution for day ${d} and task ${t} does not exist!"
      exit 2
    elif [ ! -r day${d}_task${t}.in ]; then
      echo "Input file for day ${d} and task ${t} does not exist!"
      exit 2
    fi

    solution=$( bash day${d}_task${t}.sh day${d}_task${t}.in )
    echo "Day ${d} task ${t} solution: ${solution}"
  done
done
