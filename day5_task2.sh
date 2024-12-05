#!/bin/bash

# --- Part Two ---
# While the Elves get to work printing the correctly-ordered updates, you have a
# little time to fix the rest of them.
# 
# For each of the incorrectly-ordered updates, use the page ordering rules to
# put the page numbers in the right order. For the above example, here are the
# three incorrectly-ordered updates and their correct orderings:
#  - 75,97,47,61,53 becomes 97,75,47,61,53.
#  - 61,13,29 becomes 61,29,13.
#  - 97,13,75,29,47 becomes 97,75,47,29,13.
# 
# After taking only the incorrectly-ordered updates and ordering them correctly,
# their middle page numbers are 47, 29, and 47. Adding these together produces
# 123.
# 
# Find the updates which are not in the correct order. What do you get if you
# add up the middle page numbers after correctly ordering just those updates?

function order_pages() {
  local input_file="$1"
  local rules
  local -i pages

  mapfile -t rules < <( grep -P "^\d+\|\d+$" "${input_file}" )
  read -r -a pages < <( echo "${@:2}" )

  local n_pages=${#pages[@]}
  local i=0
  local ret=0

  while [ "${i}" -lt $(( (n_pages + 3)/2 )) ]; do
    local j=$(( i + 1 ))
    while [ "${j}" -lt "${n_pages}" ]; do
      local broken_rule

      broken_rule="$( echo "${rules[*]}" | grep -Po "(${pages[${j}]}\|${pages[${i}]})" )"
      if [ -n "${broken_rule}" ]; then
        (( pages[i] += pages[j] ))
        (( pages[j] = pages[i] - pages[j] ))
        (( pages[i] -= pages[j] ))

        j=$(( i + 1 ))
        ret=1
      fi

      (( j++ ))
    done
    (( i++ ))
  done

  echo "${pages[*]}"
  return ${ret}
}

function main() {
  local input_file="$1"
  local sum=0

  while read -r line; do
    local -i pages
    local output

    read -r -d "," -a pages < <( echo "${line//,/ }" )
    output="$( order_pages "${input_file}" "${pages[*]}" )"
    if [ $? -eq 1 ]; then
      read -r -a pages < <( echo "${output[*]}" )
      (( sum += ${pages[$(( ${#pages[@]}/2 ))]} ))
    fi
  done <<< "$( grep -P "^(\d+,)+\d+$" "${input_file}" )"

  echo "${sum}"
}

if [ $# -ne 1 ]; then
  echo "$0 <task_data.in>"
  exit 1
fi

main "$1"
