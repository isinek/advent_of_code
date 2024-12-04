#!/bin/bash

# --- Day 4: Ceres Search ---
# "Looks like the Chief's not here. Next!" One of The Historians pulls out a
# device and pushes the only button on it. After a brief flash, you recognize
# the interior of the Ceres monitoring station!
# 
# As the search for the Chief continues, a small Elf who lives on the station
# tugs on your shirt; she'd like to know if you could help her with her word
# search (your puzzle input). She only has to find one word: XMAS.
# 
# This word search allows words to be horizontal, vertical, diagonal, written
# backwards, or even overlapping other words. It's a little unusual, though, as
# you don't merely need to find one instance of XMAS - you need to find all of
# them. Here are a few ways XMAS might appear, where irrelevant characters have
# been replaced with .:
# ..X...
# .SAMX.
# .A..A.
# XMAS.S
# .X....
# 
# The actual word search will be full of letters instead. For example:
# MSAMXMSMSA
# AMXSXMAAMM
# MSAMASMSMX
# XMASAMXAMM
# XXAMMXXAMA
# SMSMSASXSS
# SAXAMASAAA
# MAMMMXMMMM
# MXMXAXMASX
# 
# In this word search, XMAS occurs a total of 18 times; here's the same word
# search again, but where letters not involved in any XMAS have been replaced
# with .:
# .SAMXMS...
# ...S..A...
# ..A.A.MS.X
# XMASAMX.MM
# X.....XA.A
# S.S.S.S.SS
# .A.A.A.A.A
# ..M.M.M.MM
# .X.X.XMASX
# 
# Take a look at the little Elf's word search. How many times does XMAS appear?

function main() {
  local input_file=$1
  local map
  local n_xmas=0

  mapfile map < "${input_file}"

  for i in $( seq 0 "$(( ${#map[@]} - 1 ))" ); do
    for j in $( seq 0 "$(( ${#map[${i}]} - 2 ))" ); do
      if [[ "${map[${i}]:${j}:1}" != "X" ]]; then
        continue
      fi

      if [ "${i}" -gt 2 ]; then
        local tmp="${map[$(( i - 1 ))]:${j}:1}${map[$(( i - 2 ))]:${j}:1}${map[$(( i - 3 ))]:${j}:1}"

        if [[ "${tmp}" == "MAS" ]]; then
          (( n_xmas++ ))
        fi
      fi
      if [ "${i}" -lt $(( ${#map} - 4 )) ]; then
        local tmp="${map[$(( i + 1 ))]:${j}:1}${map[$(( i + 2 ))]:${j}:1}${map[$(( i + 3 ))]:${j}:1}"

        if [[ "${tmp}" == "MAS" ]]; then
          (( n_xmas++ ))
        fi
      fi
      if [ "${j}" -gt 2 ]; then
        local tmp="${map[${i}]:$(( j - 1 )):1}${map[${i}]:$(( j - 2 )):1}${map[${i}]:$(( j - 3 )):1}"

        if [[ "${tmp}" == "MAS" ]]; then
          (( n_xmas++ ))
        fi
      fi
      if [ "${j}" -lt $(( ${#map[${i}]} - 4 )) ]; then
        local tmp="${map[${i}]:$(( j + 1 )):1}${map[${i}]:$(( j + 2 )):1}${map[${i}]:$(( j + 3 )):1}"

        if [[ "${tmp}" == "MAS" ]]; then
          (( n_xmas++ ))
        fi
      fi

      if [ "${i}" -gt 2 ] && [ "${j}" -gt 2 ]; then
        local tmp="${map[$(( i - 1 ))]:$(( j - 1 )):1}${map[$(( i - 2 ))]:$(( j - 2 )):1}${map[$(( i - 3 ))]:$(( j - 3 )):1}"

        if [[ "${tmp}" == "MAS" ]]; then
          (( n_xmas++ ))
        fi
      fi
      if [ "${i}" -gt 2 ] && [ "${j}" -lt $(( ${#map[${i}]} - 4 )) ]; then
        local tmp="${map[$(( i - 1 ))]:$(( j + 1 )):1}${map[$(( i - 2 ))]:$(( j + 2 )):1}${map[$(( i - 3 ))]:$(( j + 3 )):1}"

        if [[ "${tmp}" == "MAS" ]]; then
          (( n_xmas++ ))
        fi
      fi
      if [ "${i}" -lt $(( ${#map} - 4 )) ] && [ "${j}" -gt 2 ]; then
        local tmp="${map[$(( i + 1 ))]:$(( j - 1 )):1}${map[$(( i + 2 ))]:$(( j - 2 )):1}${map[$(( i + 3 ))]:$(( j - 3 )):1}"

        if [[ "${tmp}" == "MAS" ]]; then
          (( n_xmas++ ))
        fi
      fi
      if [ "${i}" -lt $(( ${#map} - 4 )) ] && [ "${j}" -lt $(( ${#map[${i}]} - 4 )) ]; then
        local tmp="${map[$(( i + 1 ))]:$(( j + 1 )):1}${map[$(( i + 2 ))]:$(( j + 2 )):1}${map[$(( i + 3 ))]:$(( j + 3 )):1}"

        if [[ "${tmp}" == "MAS" ]]; then
          (( n_xmas++ ))
        fi
      fi
    done
  done

  echo ${n_xmas}
}

if [ $# -ne 1 ]; then
  echo "$0 <task_data.in>"
  exit 1
fi

main "$1"
