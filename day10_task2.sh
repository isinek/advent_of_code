#!/bin/bash

# --- Part Two ---
# The reindeer spends a few minutes reviewing your hiking trail map before
# realizing something, disappearing for a few minutes, and finally returning
# with yet another slightly-charred piece of paper.
# 
# The paper describes a second way to measure a trailhead called its rating. A
# trailhead's rating is the number of distinct hiking trails which begin at that
# trailhead. For example:
# .....0.
# ..4321.
# ..5..2.
# ..6543.
# ..7..4.
# ..8765.
# ..9....
# 
# The above map has a single trailhead; its rating is 3 because there are
# exactly three distinct hiking trails which begin at that position:
# .....0.   .....0.   .....0.
# ..4321.   .....1.   .....1.
# ..5....   .....2.   .....2.
# ..6....   ..6543.   .....3.
# ..7....   ..7....   .....4.
# ..8....   ..8....   ..8765.
# ..9....   ..9....   ..9....
# 
# Here is a map containing a single trailhead with rating 13:
# ..90..9
# ...1.98
# ...2..7
# 6543456
# 765.987
# 876....
# 987....
# 
# This map contains a single trailhead with rating 227 (because there are 121
# distinct hiking trails that lead to the 9 on the right edge and 106 that lead
# to the 9 on the bottom edge):
# 012345
# 123456
# 234567
# 345678
# 4.6789
# 56789.
# 
# Here's the larger example from before:
# 89010123
# 78121874
# 87430965
# 96549874
# 45678903
# 32019012
# 01329801
# 10456732
# 
# Considering its trailheads in reading order, they have ratings of 20, 24, 10,
# 4, 1, 4, 5, 8, and 5. The sum of all trailhead ratings in this larger example
# topographic map is 81.
# 
# You're not sure how, but the reindeer seems to have crafted some tiny flags
# out of toothpicks and bits of paper and is using them to mark trailheads on
# your topographic map. What is the sum of the ratings of all trailheads?

declare map=()

function trailhead_rating() {
  local score=0
  local next_q=( "$1,$2" )
  local peaks=()

  if [ "${map[${x}]:${y}:1}" -eq 9 ]; then
    echo "${x},${y}"
    return
  fi

  while [ -n "${next_q[*]}" ]; do
    local x="${next_q[0]%,*}"
    local y="${next_q[0]#*,}"

    next_q=( "${next_q[@]:1}" )

    if [ "${map[${x}]:${y}:1}" -eq "9" ]; then
      peaks=( "${peaks[@]}" "${x},${y}" )
      continue
    fi

    local xx="$(( x - 1 ))"
    local yy="${y}"
    if [ "${xx}" -ge 0 ] && [ "${yy}" -ge 0 ] && \
        [ -n "${map[${xx}]:${yy}:1}" ] && \
        [ "${map[${xx}]:${yy}:1}" -eq "$(( ${map[${x}]:${y}:1} + 1 ))" ]; then
      next_q=( "${next_q[@]}" "${xx},${yy}" )
    fi

    xx="$(( x + 1 ))"
    yy="${y}"
    if [ "${xx}" -ge 0 ] && [ "${yy}" -ge 0 ] && \
        [ -n "${map[${xx}]:${yy}:1}" ] && \
        [ "${map[${xx}]:${yy}:1}" -eq "$(( ${map[${x}]:${y}:1} + 1 ))" ]; then
      next_q=( "${next_q[@]}" "${xx},${yy}" )
    fi

    xx="${x}"
    yy="$(( y - 1 ))"
    if [ "${xx}" -ge 0 ] && [ "${yy}" -ge 0 ] && \
        [ -n "${map[${xx}]:${yy}:1}" ] && \
        [ "${map[${xx}]:${yy}:1}" -eq "$(( ${map[${x}]:${y}:1} + 1 ))" ]; then
      next_q=( "${next_q[@]}" "${xx},${yy}" )
    fi

    xx="${x}"
    yy="$(( y + 1 ))"
    if [ "${xx}" -ge 0 ] && [ "${yy}" -ge 0 ] && \
        [ -n "${map[${xx}]:${yy}:1}" ] && \
        [ "${map[${xx}]:${yy}:1}" -eq "$(( ${map[${x}]:${y}:1} + 1 ))" ]; then
      next_q=( "${next_q[@]}" "${xx},${yy}" )
    fi
  done

  printf "%s\n" "${peaks[@]}" | wc -l
}

function main() {
  local input_file="$1"
  local score=0

  mapfile -t map < "${input_file}"

  while read -r line; do
    local i=$(( ${line%:*} - 1 ))
    local line="${line#*:}"

    for j in $( seq 0 $(( ${#line} - 1 )) ); do
      if [[ "${map[${i}]:j:1}" != "0" ]]; then
        continue
      fi

      score=$(( score + $( trailhead_rating "${i}" "${j}" ) ))
    done
  done < <( grep -n 0 "${input_file}" )

  echo "${score}"
}

if [ $# -ne 1 ]; then
  echo "$0 <task_data.in>"
  exit 1
fi

main "$1"
