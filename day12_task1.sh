#!/bin/bash

# --- Day 12: Garden Groups ---
# Why not search for the Chief Historian near the gardener and his massive farm?
# There's plenty of food, so The Historians grab something to eat while they
# search.
# 
# You're about to settle near a complex arrangement of garden plots when some
# Elves ask if you can lend a hand. They'd like to set up fences around each
# region of garden plots, but they can't figure out how much fence they need to
# order or how much it will cost. They hand you a map (your puzzle input) of the
# garden plots.
# 
# Each garden plot grows only a single type of plant and is indicated by a
# single letter on your map. When multiple garden plots are growing the same
# type of plant and are touching (horizontally or vertically), they form a
# region. For example:
# AAAA
# BBCD
# BBCC
# EEEC
# 
# This 4x4 arrangement includes garden plots growing five different types of
# plants (labeled A, B, C, D, and E), each grouped into their own region.
# 
# In order to accurately calculate the cost of the fence around a single region,
# you need to know that region's area and perimeter.
# 
# The area of a region is simply the number of garden plots the region contains.
# The above map's type A, B, and C plants are each in a region of area 4. The
# type E plants are in a region of area 3; the type D plants are in a region of
# area 1.
# 
# Each garden plot is a square and so has four sides. The perimeter of a region
# is the number of sides of garden plots in the region that do not touch another
# garden plot in the same region. The type A and C plants are each in a region
# with perimeter 10. The type B and E plants are each in a region with perimeter
# 8. The lone D plot forms its own region with perimeter 4.
# 
# Visually indicating the sides of plots in each region that contribute to the
# perimeter using - and |, the above map's regions' perimeters are measured as
# follows:
# +-+-+-+-+
# |A A A A|
# +-+-+-+-+     +-+
#               |D|
# +-+-+   +-+   +-+
# |B B|   |C|
# +   +   + +-+
# |B B|   |C C|
# +-+-+   +-+ +
#           |C|
# +-+-+-+   +-+
# |E E E|
# +-+-+-+
# 
# Plants of the same type can appear in multiple separate regions, and regions
# can even appear within other regions. For example:
# OOOOO
# OXOXO
# OOOOO
# OXOXO
# OOOOO
# 
# The above map contains five regions, one containing all of the O garden plots,
# and the other four each containing a single X plot.
# 
# The four X regions each have area 1 and perimeter 4. The region containing 21
# type O plants is more complicated; in addition to its outer edge contributing
# a perimeter of 20, its boundary with each X region contributes an additional 4
# to its perimeter, for a total perimeter of 36.
# 
# Due to "modern" business practices, the price of fence required for a region
# is found by multiplying that region's area by its perimeter. The total price
# of fencing all regions on a map is found by adding together the price of fence
# for every region on the map.
# 
# In the first example, region A has price 4 * 10 = 40, region B has price
# 4 * 8 = 32, region C has price 4 * 10 = 40, region D has price 1 * 4 = 4, and
# region E has price 3 * 8 = 24. So, the total price for the first example is
# 140.
# 
# In the second example, the region with all of the O plants has price
# 21 * 36 = 756, and each of the four smaller X regions has price 1 * 4 = 4, for
# a total price of 772 (756 + 4 + 4 + 4 + 4).
# 
# Here's a larger example:
# RRRRIICCFF
# RRRRIICCCF
# VVRRRCCFFF
# VVRCCCJFFF
# VVVVCJJCFE
# VVIVCCJJEE
# VVIIICJJEE
# MIIIIIJJEE
# MIIISIJEEE
# MMMISSJEEE
# 
# It contains:
#  - A region of R plants with price 12 * 18 = 216.
#  - A region of I plants with price 4 * 8 = 32.
#  - A region of C plants with price 14 * 28 = 392.
#  - A region of F plants with price 10 * 18 = 180.
#  - A region of V plants with price 13 * 20 = 260.
#  - A region of J plants with price 11 * 20 = 220.
#  - A region of C plants with price 1 * 4 = 4.
#  - A region of E plants with price 13 * 18 = 234.
#  - A region of I plants with price 14 * 22 = 308.
#  - A region of M plants with price 5 * 12 = 60.
#  - A region of S plants with price 3 * 8 = 24.
# 
# So, it has a total price of 1930.
# 
# What is the total price of fencing all regions on your map?

declare map=()

function calculate_price() {
  local q=( "$1,$2" )
  local label="${map[$1]:$2:1}"
  local area=0
  local perimeter=0

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
      (( perimeter++ ))
    fi

    xxx=$(( xx + 1 ))
    yyy=${yy}
    if [[ "${map[${xxx}]:${yyy}:1}" == "${label}" ]] && \
        [[ ! " ${q[*]} " =~ " ${xxx},${yyy} " ]] && \
        grep -q "^${xxx} ${yyy}$" not_visited.tmp; then
      q=( "${q[@]}" "${xxx},${yyy}" )
    elif [[ "${map[${xxx}]:${yyy}:1}" != "${label}" ]]; then
      (( perimeter++ ))
    fi

    xxx=${xx}
    yyy=$(( yy - 1 ))
    if [[ "${map[${xxx}]:${yyy}:1}" == "${label}" ]] && \
        [[ ! " ${q[*]} " =~ " ${xxx},${yyy} " ]] && \
        grep -q "^${xxx} ${yyy}$" not_visited.tmp; then
      q=( "${q[@]}" "${xxx},${yyy}" )
    elif [ "${yyy}" -lt 0 ] || [[ "${map[${xxx}]:${yyy}:1}" != "${label}" ]]; then
      (( perimeter++ ))
    fi

    xxx=${xx}
    yyy=$(( yy + 1 ))
    if [[ "${map[${xxx}]:${yyy}:1}" == "${label}" ]] && \
        [[ ! " ${q[*]} " =~ " ${xxx},${yyy} " ]] && \
        grep -q "^${xxx} ${yyy}$" not_visited.tmp; then
      q=( "${q[@]}" "${xxx},${yyy}" )
    elif [[ "${map[${xxx}]:${yyy}:1}" != "${label}" ]]; then
      (( perimeter++ ))
    fi

    grep -v "^${xx} ${yy}$" not_visited.tmp > tmp
    mv tmp not_visited.tmp
  done

  echo "$(( area*perimeter ))"
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
}

if [ $# -ne 1 ]; then
  echo "$0 <task_data.in>"
  exit 1
fi

main "$1"
