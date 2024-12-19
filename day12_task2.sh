#!/bin/bash

# --- Part Two ---
# Fortunately, the Elves are trying to order so much fence that they qualify for
# a bulk discount!
# 
# Under the bulk discount, instead of using the perimeter to calculate the
# price, you need to use the number of sides each region has. Each straight
# section of fence counts as a side, regardless of how long it is.
# 
# Consider this example again:
# AAAA
# BBCD
# BBCC
# EEEC
# 
# The region containing type A plants has 4 sides, as does each of the regions
# containing plants of type B, D, and E. However, the more complex region
# containing the plants of type C has 8 sides!
# 
# Using the new method of calculating the per-region price by multiplying the
# region's area by its number of sides, regions A through E have prices 16, 16,
# 32, 4, and 12, respectively, for a total price of 80.
# 
# The second example above (full of type X and O plants) would have a total
# price of 436.
# 
# Here's a map that includes an E-shaped region full of type E plants:
# EEEEE
# EXXXX
# EEEEE
# EXXXX
# EEEEE
# 
# The E-shaped region has an area of 17 and 12 sides for a price of 204.
# Including the two regions full of type X plants, this map has a total price of
# 236.
# 
# This map has a total price of 368:
# AAAAAA
# AAABBA
# AAABBA
# ABBAAA
# ABBAAA
# AAAAAA
# 
# It includes two regions full of type B plants (each with 4 sides) and a single
# region full of type A plants (with 4 sides on the outside and 8 more sides on
# the inside, a total of 12 sides). Be especially careful when counting the
# fence around regions like the one full of type A plants; in particular, each
# section of fence has an in-side and an out-side, so the fence does not connect
# across the middle of the region (where the two B regions touch diagonally).
# (The Elves would have used the Möbius Fencing Company instead, but their
# contract terms were too one-sided.)
# 
# The larger example from before now has the following updated prices:
#  - A region of R plants with price 12 * 10 = 120.
#  - A region of I plants with price 4 * 4 = 16.
#  - A region of C plants with price 14 * 22 = 308.
#  - A region of F plants with price 10 * 12 = 120.
#  - A region of V plants with price 13 * 10 = 130.
#  - A region of J plants with price 11 * 12 = 132.
#  - A region of C plants with price 1 * 4 = 4.
#  - A region of E plants with price 13 * 8 = 104.
#  - A region of I plants with price 14 * 16 = 224.
#  - A region of M plants with price 5 * 6 = 30.
#  - A region of S plants with price 3 * 6 = 18.
# 
# Adding these together produces its new total price of 1206.
# 
# What is the new total price of fencing all regions on your map?

declare map=()

function calculate_price() {
  local q=( "$1,$2" )
  local label="${map[$1]:$2:1}"
  local area=0

  touch perimeter.tmp
  while [ "${#q[@]}" -gt 0 ]; do
    local xx="${q[0]%,*}"
    local yy="${q[0]#*,}"
    q=( "${q[@]:1}" )

    (( area++ ))

    local xxx=$(( xx - 1 ))
    local yyy=${yy}
    if [[ "${map[${xxx}]:${yyy}:1}" == "${label}" ]] && \
        [[ ! " ${q[*]} " =~ " ${xxx},${yyy} " ]] && \
        grep -q "^${xxx} ${yyy}$" not_visited.tmp; then
      q=( "${q[@]}" "${xxx},${yyy}" )
    elif [ "${xxx}" -lt 0 ] || [[ "${map[${xxx}]:${yyy}:1}" != "${label}" ]]; then
      echo "${xxx},${yyy}" >> perimeter.tmp
    fi

    xxx=$(( xx + 1 ))
    yyy=${yy}
    if [[ "${map[${xxx}]:${yyy}:1}" == "${label}" ]] && \
        [[ ! " ${q[*]} " =~ " ${xxx},${yyy} " ]] && \
        grep -q "^${xxx} ${yyy}$" not_visited.tmp; then
      q=( "${q[@]}" "${xxx},${yyy}" )
    elif [[ "${map[${xxx}]:${yyy}:1}" != "${label}" ]]; then
      echo "${xxx},${yyy}" >> perimeter.tmp
    fi

    xxx=${xx}
    yyy=$(( yy - 1 ))
    if [[ "${map[${xxx}]:${yyy}:1}" == "${label}" ]] && \
        [[ ! " ${q[*]} " =~ " ${xxx},${yyy} " ]] && \
        grep -q "^${xxx} ${yyy}$" not_visited.tmp; then
      q=( "${q[@]}" "${xxx},${yyy}" )
    elif [ "${yyy}" -lt 0 ] || [[ "${map[${xxx}]:${yyy}:1}" != "${label}" ]]; then
      echo "${xxx},${yyy}" >> perimeter.tmp
    fi

    xxx=${xx}
    yyy=$(( yy + 1 ))
    if [[ "${map[${xxx}]:${yyy}:1}" == "${label}" ]] && \
        [[ ! " ${q[*]} " =~ " ${xxx},${yyy} " ]] && \
        grep -q "^${xxx} ${yyy}$" not_visited.tmp; then
      q=( "${q[@]}" "${xxx},${yyy}" )
    elif [[ "${map[${xxx}]:${yyy}:1}" != "${label}" ]]; then
      echo "${xxx},${yyy}" >> perimeter.tmp
    fi

    grep -v "^${xx} ${yy}$" not_visited.tmp > tmp
    mv tmp not_visited.tmp
  done

  mapfile -t perimeter < <( cat perimeter.tmp | sort -t ',' -k 1,1n -k 2,2n )
  rm -f perimeter.tmp
  touch perimeter.tmp
  echo -n "${label} - ${area} ${#perimeter[@]}" >&2

  local sides=0
  while [ "${#perimeter[@]}" -gt 0 ]; do
    local xx="${perimeter[0]%,*}"
    local yy="${perimeter[0]#*,}"

    if [[ " ${perimeter[*]} " =~ " $(( xx + 1 )),${yy} " ]]; then
      (( sides++ ))

      local i=0
      while [[ " ${perimeter[*]} " =~ " $(( xx + i )),${yy} " ]]; do
        mapfile -t perimeter < <( printf "%s\n" "${perimeter[@]}" | \
            sed "0,/^$(( xx + i )),${yy}$/s///" )
        (( i++ ))
      done
      mapfile -t perimeter < <( printf "%s\n" "${perimeter[@]}" | grep -v "^$" )
    elif [[ " ${perimeter[*]} " =~ " ${xx},$(( yy + 1 )) " ]]; then
      (( sides++ ))

      local i=0
      while [[ " ${perimeter[*]} " =~ " ${xx},$(( yy + i )) " ]]; do
        mapfile -t perimeter < <( printf "%s\n" "${perimeter[@]}" | \
            sed "0,/^${xx},$(( yy + i ))$/s///" )
        (( i++ ))
      done
      mapfile -t perimeter < <( printf "%s\n" "${perimeter[@]}" | grep -v "^$" )
    else
      echo "${perimeter[0]}" >> perimeter.tmp
      perimeter=( "${perimeter[@]:1}" )
    fi
  done

  echo -n " $( cat perimeter.tmp | wc -l )" >&2
  (( sides += "$( cat perimeter.tmp | wc -l )" ))

  echo " ${sides}" >&2
  echo "$(( area*sides ))"

  rm -f perimeter.tmp
}

function main() {
  local input_file=$1
  local sum=0

  mapfile -t map < "${input_file}"

  touch not_visited.tmp
  for i in $( seq 0 $(( "${#map[@]}" - 1 )) ); do
    for j in $( seq 0 $(( "${#map[${i}]}" - 1 )) ); do
      echo "${i} ${j}" >> not_visited.tmp
    done
  done

  while [ -n "$( head -1 not_visited.tmp )" ]; do
    read -r x y < <( head -1 not_visited.tmp )
    sum=$(( sum + $( calculate_price "${x}" "${y}" ) ))
  done

  echo "${sum}"
  rm -f not_visited.tmp
}

if [ $# -ne 1 ]; then
  echo "$0 <task_data.in>"
  exit 1
fi

main "$1"
