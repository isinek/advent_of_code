#!/bin/bash

# --- Part Two ---
# The Elf looks quizzically at you. Did you misunderstand the assignment?
# 
# Looking for the instructions, you flip over the word search to find that this
# isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed
# to find two MAS in the shape of an X. One way to achieve that is like this:
# M.S
# .A.
# M.S
# 
# Irrelevant characters have again been replaced with . in the above diagram.
# Within the X, each MAS can be written forwards or backwards.
# 
# Here's the same example from before, but this time all of the X-MASes have
# been kept instead:
# .M.S......
# ..A..MSMS.
# .M.S.MAA..
# ..A.ASMSM.
# .M.S.M....
# ..........
# S.S.S.S.S.
# .A.A.A.A..
# M.M.M.M.M.
# ..........
# 
# In this example, an X-MAS appears 9 times.
# 
# Flip the word search from the instructions back over to the word search side
# and try again. How many times does an X-MAS appear?

function main() {
  local input_file=$1
  local map
  local n_xmas=0

  mapfile map < "${input_file}"

  for i in $( seq 0 "$(( ${#map[@]} - 3 ))" ); do
    for j in $( seq 0 "$(( ${#map[${i}]} - 4 ))" ); do
      local tmp="${map[${i}]:${j}:1}${map[${i}]:$(( j + 2 )):1}${map[$(( i + 1 ))]:$(( j + 1 )):1}${map[$(( i + 2 ))]:${j}:1}${map[$(( i + 2 ))]:$(( j + 2 )):1}"

      if [[ "${tmp}" =~ (MMASS|MSAMS|SMASM|SSAMM) ]]; then
        (( n_xmas++ ))
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
