#!/bin/bash

# --- Day 8: Resonant Collinearity ---
# You find yourselves on the roof of a top-secret Easter Bunny installation.
# 
# While The Historians do their thing, you take a look at the familiar huge
# antenna. Much to your surprise, it seems to have been reconfigured to emit a
# signal that makes people 0.1% more likely to buy Easter Bunny brand Imitation
# Mediocre Chocolate as a Christmas gift! Unthinkable!
# 
# Scanning across the city, you find that there are actually many such antennas.
# Each antenna is tuned to a specific frequency indicated by a single lowercase
# letter, uppercase letter, or digit. You create a map (your puzzle input) of
# these antennas. For example:
# ............
# ........0...
# .....0......
# .......0....
# ....0.......
# ......A.....
# ............
# ............
# ........A...
# .........A..
# ............
# ............
# 
# The signal only applies its nefarious effect at specific antinodes based on
# the resonant frequencies of the antennas. In particular, an antinode occurs at
# any point that is perfectly in line with two antennas of the same frequency -
# but only when one of the antennas is twice as far away as the other. This
# means that for any pair of antennas with the same frequency, there are two
# antinodes, one on either side of them.
# 
# So, for these two antennas with frequency a, they create the two antinodes
# marked with #:
# ..........
# ...#......
# ..........
# ....a.....
# ..........
# .....a....
# ..........
# ......#...
# ..........
# ..........
# 
# Adding a third antenna with the same frequency creates several more antinodes.
# It would ideally add four antinodes, but two are off the right side of the
# map, so instead it adds only two:
# ..........
# ...#......
# #.........
# ....a.....
# ........a.
# .....a....
# ..#.......
# ......#...
# ..........
# ..........
# 
# Antennas with different frequencies don't create antinodes; A and a count as
# different frequencies. However, antinodes can occur at locations that contain
# antennas. In this diagram, the lone antenna with frequency capital A creates
# no antinodes but has a lowercase-a-frequency antinode at its location:
# ..........
# ...#......
# #.........
# ....a.....
# ........a.
# .....a....
# ..#.......
# ......A...
# ..........
# ..........
# 
# The first example has antennas with two different frequencies, so the
# antinodes they create look like this, plus an antinode overlapping the topmost
# A-frequency antenna:
# ......#....#
# ...#....0...
# ....#0....#.
# ..#....0....
# ....0....#..
# .#....A.....
# ...#........
# #......#....
# ........A...
# .........A..
# ..........#.
# ..........#.
# 
# Because the topmost A-frequency antenna overlaps with a 0-frequency antinode,
# there are 14 total unique locations that contain an antinode within the bounds
# of the map.
# 
# Calculate the impact of the signal. How many unique locations within the
# bounds of the map contain an antinode?

function main() {
  local input_file="$1"
  local height=0
  local width=0
  local antinodes=()

  while read -r line; do
    width="${#line}"

    for j in $( seq 0 $(( ${#line} - 1 )) ); do
      if [[ "${line:${j}:1}" == "." ]]; then
        continue
      fi

      local antenna="antenna_${line:${j}:1}.tmp"
      touch "${antenna}"
      echo "${height},${j}" >> "${antenna}"
    done

    (( height++ ))
  done < "${input_file}"

  for antenna in antenna_*.tmp; do
    local nodes=()

    while read -r current; do
      for x in "${nodes[@]}"; do
        local new_antinode=

        new_antinode="$(( "${current%,*}"*2 - "${x%,*}" )),$(( "${current#*,}"*2 - "${x#*,}" ))"
        if [ "${new_antinode%,*}" -ge 0 ] && [ "${new_antinode#*,}" -ge 0 ] && \
            [ "${new_antinode%,*}" -lt "${height}" ] && \
            [ "${new_antinode#*,}" -lt "${width}" ] && \
            [[ ! " ${antinodes[*]} " =~ " ${new_antinode} " ]]; then
          antinodes=( "${antinodes[@]}" "${new_antinode}" )
        fi

        new_antinode="$(( "${x%,*}"*2 - "${current%,*}" )),$(( "${x#*,}"*2 - "${current#*,}" ))"
        if [ "${new_antinode%,*}" -ge 0 ] && [ "${new_antinode#*,}" -ge 0 ] && \
            [ "${new_antinode%,*}" -lt "${height}" ] && \
            [ "${new_antinode#*,}" -lt "${width}" ] && \
            [[ ! " ${antinodes[*]} " =~ " ${new_antinode} " ]]; then
          antinodes=( "${antinodes[@]}" "${new_antinode}" )
        fi
      done

      nodes=( "${nodes[@]}" "${current}" )
    done < "${antenna}"
  done

  echo "${#antinodes[@]}"

  rm -f ./antenna_*.tmp
}

if [ $# -ne 1 ]; then
  echo "$0 <task_data.in>"
  exit 1
fi

main "$1"
