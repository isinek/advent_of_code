#!/bin/bash

# --- Part Two ---
# The engineers seem concerned; the total calibration result you gave them is
# nowhere close to being within safety tolerances. Just then, you spot your
# mistake: some well-hidden elephants are holding a third type of operator.
# 
# The concatenation operator (||) combines the digits from its left and right
# inputs into a single number. For example, 12 || 345 would become 12345. All
# operators are still evaluated left-to-right.
# 
# Now, apart from the three equations that could be made true using only
# addition and multiplication, the above example has three more equations that
# can be made true by inserting operators:
#  - 156: 15 6 can be made true through a single concatenation: 15 || 6 = 156.
#  - 7290: 6 8 6 15 can be made true using 6 * 8 || 6 * 15.
#  - 192: 17 8 14 can be made true using 17 || 8 + 14.
# 
# Adding up all six test values (the three that could be made before using only
# + and * plus the new three that can now be made by also using ||) produces the
# new total calibration result of 11387.
# 
# Using your new knowledge of elephant hiding spots, determine which equations
# could possibly be true. What is their total calibration result?


function is_valid_equation() {
  local expected_result="$1"
  local -i operands

  read -r -a operands < <( echo "${@:2}" )

  echo "${operands[0]}" > result_q.tmp
  for x in "${operands[@]:1}"; do
    touch new_result_q.tmp

    while read -r result; do
      local tmp=$(( result + x ))
      if [ "${tmp}" -le "${expected_result}" ]; then
        echo "${tmp}" >> new_result_q.tmp
      fi

      tmp=$(( result*x ))
      if [ "${tmp}" -le "${expected_result}" ]; then
        echo "${tmp}" >> new_result_q.tmp
      fi

      tmp="${result}${x}"
      if [ "${tmp}" -le "${expected_result}" ]; then
        echo "${tmp}" >> new_result_q.tmp
      fi
    done < result_q.tmp

    if [ ! -f new_result_q.tmp ]; then
      break
    fi

    mv new_result_q.tmp result_q.tmp
  done

  if grep -q "${expected_result}" result_q.tmp; then
    return 0
  fi

  return 1
}

function main() {
  local input_file="$1"
  local sum=0

  while read -r equation; do
    local expected_result="${equation%:*}"

    if is_valid_equation "${expected_result}" "${equation#*:}"; then
      sum=$(( sum + expected_result ))
    fi

    rm -f result_q.tmp
  done < "${input_file}"

  echo "${sum}"
}

if [ $# -ne 1 ]; then
  echo "$0 <task_data.in>"
  exit 1
fi

main "$1"
