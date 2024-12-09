#!/bin/bash

# --- Part Two ---
# Watching over your shoulder as you work, one of The Historians asks if you
# took the effects of resonant harmonics into your calculations.
# 
# Whoops!
# 
# After updating your model, it turns out that an antinode occurs at any grid
# position exactly in line with at least two antennas of the same frequency,
# regardless of distance. This means that some of the new antinodes will occur
# at the position of each antenna (unless that antenna is the only one of its
# frequency).
# 
# So, these three T-frequency antennas now create many antinodes:
# T....#....
# ...T......
# .T....#...
# .........#
# ..#.......
# ..........
# ...#......
# ..........
# ....#.....
# ..........
# 
# In fact, the three T-frequency antennas are all exactly in line with two
# antennas, so they are all also antinodes! This brings the total number of
# antinodes in the above example to 9.
# 
# The original example now has 34 antinodes, including the antinodes that appear
# on every antenna:
# ##....#....#
# .#.#....0...
# ..#.#0....#.
# ..##...0....
# ....0....#..
# .#...#A....#
# ...#..#.....
# #....#.#....
# ..#.....A...
# ....#....A..
# .#........#.
# ...#......##
# 
# Calculate the impact of the signal using this updated model. How many unique
# locations within the bounds of the map contain an antinode?

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
        local diff=

        diff=( "$(( "${current%,*}" - "${x%,*}" ))" "$(( "${current#*,}" - "${x#*,}" ))" )
        for i in $( seq -50 50 ); do
          new_antinode="$(( "${current%,*}" - diff[0]*i )),$(( "${current#*,}" - diff[1]*i ))"
          if [ "${new_antinode%,*}" -lt 0 ] || \
              [ "${new_antinode#*,}" -lt 0 ] || \
              [ "${new_antinode%,*}" -ge "${height}" ] || \
              [ "${new_antinode#*,}" -ge "${width}" ]; then
            continue
          elif [[ ! " ${antinodes[*]} " =~ " ${new_antinode} " ]]; then
            antinodes=( "${antinodes[@]}" "${new_antinode}" )
          fi

          (( i++ ))
        done

        diff=( "$(( "${current%,*}" - "${x%,*}" ))" "$(( "${current#*,}" - "${x#*,}" ))" )
        for i in $( seq -50 50 ); do
          new_antinode="$(( "${x%,*}" - diff[0]*i )),$(( "${x#*,}" - diff[1]*i ))"
          if [ "${new_antinode%,*}" -lt 0 ] || \
              [ "${new_antinode#*,}" -lt 0 ] || \
              [ "${new_antinode%,*}" -ge "${height}" ] || \
              [ "${new_antinode#*,}" -ge "${width}" ]; then
            continue
          elif [[ ! " ${antinodes[*]} " =~ " ${new_antinode} " ]]; then
            antinodes=( "${antinodes[@]}" "${new_antinode}" )
          fi

          (( i++ ))
        done
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
