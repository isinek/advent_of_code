#!/bin/bash

# --- Part Two ---
# As you go to win the first prize, you discover that the claw is nowhere near
# where you expected it would be. Due to a unit conversion error in your
# measurements, the position of every prize is actually 10000000000000 higher on
# both the X and Y axis!
# 
# Add 10000000000000 to the X and Y position of every prize. After making this
# change, the example above would now look like this:
# Button A: X+94, Y+34
# Button B: X+22, Y+67
# Prize: X=10000000008400, Y=10000000005400
# 
# Button A: X+26, Y+66
# Button B: X+67, Y+21
# Prize: X=10000000012748, Y=10000000012176
# 
# Button A: X+17, Y+86
# Button B: X+84, Y+37
# Prize: X=10000000007870, Y=10000000006450
# 
# Button A: X+69, Y+23
# Button B: X+27, Y+71
# Prize: X=10000000018641, Y=10000000010279
# 
# Now, it is only possible to win a prize on the second and fourth claw
# machines. Unfortunately, it will take many more than 100 presses to do so.
# 
# Using the corrected prize coordinates, figure out how to win as many prizes as
# possible. What is the fewest tokens you would have to spend to win all
# possible prizes?

function main() {
  local input_file=$1
  local -i a=()
  local -i b=()
  local -i prize=()
  local sum=0

  while read -r line; do
    if [[ "${line:7:1}" == "A" ]]; then
      mapfile -t a < <( echo "${line}" | grep -o "[0-9]\+" )
      continue
    elif [[ "${line:7:1}" == "B" ]]; then
      mapfile -t b < <( echo "${line}" | grep -o "[0-9]\+" )
      continue
    elif [ "${#line}" -eq 0 ]; then
      continue
    fi

    mapfile -t prize < <( echo "${line}" | grep -o "[0-9]\+" )
    (( prize[0] += 10000000000000 ))
    (( prize[1] += 10000000000000 ))

    local price=99999999999999
    local i=0
    local ii=1
    while [ $(( i*a[0] )) -lt "${prize[0]}" ] && [ $(( i*a[1] )) -lt "${prize[1]}" ]; do
      local x=$(( (prize[0] - i*a[0])/b[0] ))
      if [ $(( i*a[0] + x*b[0] )) -eq "${prize[0]}" ] && \
          [ $(( i*a[1] + x*b[1] )) -eq "${prize[1]}" ]; then
        local tmp_price=$(( i*3 + x ))
        if [ "${tmp_price}" -lt "${price}" ]; then
          price="${tmp_price}"
        else
          break
        fi

        if [ "${ii}" -eq 1 ]; then
          ii="${i}"
        fi
      fi
      (( i += ii ))
    done

    if [ "${price}" -lt 99999999999999 ]; then
      (( sum += price ))
    fi
  done < "${input_file}"

  echo "${sum}"
}

if [ $# -ne 1 ]; then
  echo "$0 <task_data.in>"
  exit 1
fi

main "$1"
