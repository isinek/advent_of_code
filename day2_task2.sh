#!/bin/bash

# --- Part Two ---
# The engineers are surprised by the low number of safe reports until they
# realize they forgot to tell you about the Problem Dampener.
# 
# The Problem Dampener is a reactor-mounted module that lets the reactor safety
# systems tolerate a single bad level in what would otherwise be a safe report.
# It's like the bad level never happened!
# 
# Now, the same rules apply as before, except if removing a single level from
# an unsafe report would make it safe, the report instead counts as safe.
# 
# More of the above example's reports are now safe:
# 1 2 7 8 9: Unsafe regardless of which level is removed.
# 9 7 6 2 1: Unsafe regardless of which level is removed.
# 1 3 2 4 5: Safe by removing the second level, 3.
# 8 6 4 4 1: Safe by removing the third level, 4.
# 1 3 6 7 9: Safe without removing any level.
# 
# Thanks to the Problem Dampener, 4 reports are actually safe!
# 
# Update your analysis by handling situations where the Problem Dampener can
# remove a single level from unsafe reports. How many reports are now safe?

function is_safe() {
  local problem_dampener=$1
  local -i levels
  local increase

  mapfile -d " " levels < <( echo "${@:2}" )
  increase=$(( levels[0] < levels[1] ))

  for i in $( seq 0 $(( ${#levels[@]} - 2 )) ); do
    local curr_diff=$(( ${levels[$(( i + 1 ))]} - ${levels[${i}]} ))

    if (( increase && curr_diff <= 3 && curr_diff >= 1 )); then
      continue
    elif (( ! increase && curr_diff >= -3 && curr_diff <= -1 )); then
      continue
    fi

    if (( problem_dampener )); then
      local res=0
      
      res=$( is_safe 0 "${levels[@]:0:$(( i ))}" "${levels[@]:$(( i + 1 ))}" )
      if [ "${res}" -eq 0 ]; then
        res=$( is_safe 0 "${levels[@]:0:$(( i + 1 ))}" "${levels[@]:$(( i + 2 ))}" )
      fi
      if [ "${res}" -eq 0 ] && [ "${i}" -gt 0 ]; then
        res=$( is_safe 0 "${levels[@]:1}" )
      fi
      if [ "${res}" -eq 0 ] && [ "${i}" -gt 1 ]; then
        res=$( is_safe 0 "${levels[0]}" "${levels[@]:2}" )
      fi

      echo "${res}"
      return
    else
      echo 0
    fi

    return
  done

  echo 1
}

function main() {
  local input_file=$1
  local sum=0

  while read -r line; do
    sum=$(( sum + $( is_safe 1 "${line}" ) ))
  done < "${input_file}"

  echo ${sum}
}

if [ $# -ne 1 ]; then
  echo "$0 <task_data.in>"
  exit 1
fi

main "$1"
