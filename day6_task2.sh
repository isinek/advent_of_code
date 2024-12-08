#!/bin/bash

# --- Part Two ---
# While The Historians begin working around the guard's patrol route, you
# borrow their fancy device and step outside the lab. From the safety of a
# supply closet, you time travel through the last few months and record the
# nightly status of the lab's guard post on the walls of the closet.
# 
# Returning after what seems like only a few seconds to The Historians, they
# explain that the guard's patrol area is simply too large for them to safely
# search the lab without getting caught.
# 
# Fortunately, they are pretty sure that adding a single new obstruction won't
# cause a time paradox. They'd like to place the new obstruction in such a way
# that the guard will get stuck in a loop, making the rest of the lab safe to
# search.
# 
# To have the lowest chance of creating a time paradox, The Historians would
# like to know all of the possible positions for such an obstruction. The new
# obstruction can't be placed at the guard's starting position - the guard is
# there right now and would notice.
# 
# In the above example, there are only 6 different positions where a new
# obstruction would cause the guard to get stuck in a loop. The diagrams of
# these six situations use O to mark the new obstruction, | to show a position
# where the guard moves up/down, - to show a position where the guard moves
# left/right, and + to show a position where the guard moves both up/down and
# left/right.
# 
# Option one, put a printing press next to the guard's starting position:
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ....|..#|.
# ....|...|.
# .#.O^---+.
# ........#.
# #.........
# ......#...
# 
# Option two, put a stack of failed suit prototypes in the bottom right quadrant
# of the mapped area:
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ......O.#.
# #.........
# ......#...
# 
# Option three, put a crate of chimney-squeeze prototype fabric next to the
# standing desk in the bottom right quadrant:
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# .+----+O#.
# #+----+...
# ......#...
# 
# Option four, put an alchemical retroencabulator near the bottom left corner:
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ..|...|.#.
# #O+---+...
# ......#...
# 
# Option five, put the alchemical retroencabulator a bit to the right instead:
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# ....|.|.#.
# #..O+-+...
# ......#...
# 
# Option six, put a tank of sovereign glue right next to the tank of universal
# solvent:
# ....#.....
# ....+---+#
# ....|...|.
# ..#.|...|.
# ..+-+-+#|.
# ..|.|.|.|.
# .#+-^-+-+.
# .+----++#.
# #+----++..
# ......#O..
# 
# It doesn't really matter what you choose to use as an obstacle so long as you
# and The Historians can put it into position without the guard noticing. The
# important thing is having enough options that you can find one that minimizes
# time paradoxes, and in this example, there are 6 different positions you could
# choose.
# 
# You need to get the guard stuck in a loop by adding a single new obstruction.
# How many different positions could you choose for this obstruction?

declare map=()
declare alt_obstacles=()
declare height=0
declare width=0
declare -A next_dir=( ["U"]="R" ["R"]="D" ["D"]="L" ["L"]="U" )

function is_endless_run() {
  local -i pos=( "$1" "$2" )
  local direction="$3"
  local moves=()

  while [[ ! " ${moves[*]} " =~ " ${pos[0]},${pos[1]}_${direction} " ]]; do
    local hit_obstacle=
    local new_pos=( "${pos[@]}" )

    moves=( "${moves[@]}" "${pos[0]},${pos[1]}_${direction}" )

    if [[ "${direction}" == "U" ]]; then
      hit_obstacle="$( printf "%s\n" "${alt_obstacles[@]}" |              \
              grep "^[0-9]*,${pos[1]}$" | grep -o "^[0-9]*" |             \
              awk "{ if ( int(\$1) < int(${pos[0]}) ) print int(\$1) }" | \
              tail -1 )"
      new_pos=( "$(( hit_obstacle + 1 ))" "${pos[1]}" )
    elif [[ "${direction}" == "D" ]]; then
      hit_obstacle="$( printf "%s\n" "${alt_obstacles[@]}" |              \
              grep "^[0-9]*,${pos[1]}$" | grep -o "^[0-9]*" |             \
              awk "{ if ( int(\$1) > int(${pos[0]}) ) print int(\$1) }" | \
              head -1 )"
      new_pos=( "$(( hit_obstacle - 1 ))" "${pos[1]}" )
    elif [[ "${direction}" == "L" ]]; then
      hit_obstacle="$( printf "%s\n" "${alt_obstacles[@]}" |              \
              grep "^${pos[0]},[0-9]*$" | grep -o "[0-9]*$" |             \
              awk "{ if ( int(\$1) < int(${pos[1]}) ) print int(\$1) }" | \
              tail -1 )"
      new_pos=( "${pos[0]}" "$(( hit_obstacle + 1 ))" )
    elif [[ "${direction}" == "R" ]]; then
      hit_obstacle="$( printf "%s\n" "${alt_obstacles[@]}" |              \
              grep "^${pos[0]},[0-9]*$" | grep -o "[0-9]*$" |             \
              awk "{ if ( int(\$1) > int(${pos[1]}) ) print int(\$1) }" | \
              head -1 )"
      new_pos=( "${pos[0]}" "$(( hit_obstacle - 1 ))" )
    fi

    if [ -z "${hit_obstacle}" ]; then
      return 1
    fi

    pos=( "${new_pos[@]}" )
    direction="${next_dir[${direction}]}"
  done

  return $(( ! ( pos[0] >= 0 && pos[0] < height && pos[1] >= 0 && pos[1] < width ) ))
}

function find_route() {
  local -i pos=( "$1" "$2" )
  local direction="$3"
  local -i new_pos=( "${pos[@]}" )

  while [ "${new_pos[0]}" -gt -1 ] &&        \
      [ "${new_pos[0]}" -lt "${height}" ] && \
      [ "${new_pos[1]}" -gt -1 ] &&          \
      [ "${new_pos[1]}" -lt "${width}" ]; do
    map["${pos[0]}"]="${map[${pos[0]}]:0:${pos[1]}}X${map[${pos[0]}]:$(( pos[1] + 1 ))}"

    if [[ "${direction}" == "U" ]]; then
      (( new_pos[0]-- ))
    elif [[ "${direction}" == "D" ]]; then
      (( new_pos[0]++ ))
    elif [[ "${direction}" == "L" ]]; then
      (( new_pos[1]-- ))
    elif [[ "${direction}" == "R" ]]; then
      (( new_pos[1]++ ))
    fi

    if [[ "${map[${new_pos[0]}]:${new_pos[1]}:1}" == "#" ]]; then
      direction="${next_dir[${direction}]}"
      new_pos=( "${pos[@]}" )
    fi

    pos=( "${new_pos[@]}" )
  done
}

function main() {
  local input_file="$1"
  local -i position=( 0 0 )
  local direction="U"
  local start_line=
  local obstacles=()
  local n_solutions=0

  mapfile -t map < "${input_file}"

  height="${#map[@]}"
  width="${#map[0]}"

  start_line="$( printf "%s\n" "${map[@]}" | grep -n "\^" )"
  position[0]="${start_line%:*}"
  (( position[0]-- ))

  start_line="${start_line#*:}"
  start_line="${start_line%^*}"
  position[1]="${#start_line}"

  find_route "${position[@]}" "${direction}"
  for i in $( seq 0 $(( height - 1 )) ); do
    for j in $( seq 0 $(( width - 1 )) ); do
      if [[ "${map[${i}]:${j}:1}" != "#" ]]; then
        continue
      fi

      obstacles=( "${obstacles[@]}" "${i},${j}" )
    done
  done

  for i in $( seq 0 $(( height - 1 )) ); do
    for j in $( seq 0 $(( width - 1 )) ); do
      if [[ "${map[${i}]:${j}:1}" != "X" ]]; then
        continue
      fi

      mapfile -t alt_obstacles < <(                         \
              printf "%s\n" "${obstacles[@]}" "${i},${j}" | \
              sort -n -t "," -k 1 -k 2 )
      if is_endless_run "${position[@]}" "${direction}"; then
        (( n_solutions++ ))
      fi
    done
  done

  echo "${n_solutions}"
}

if [ $# -ne 1 ]; then
  echo "$0 <task_data.in>"
  exit 1
fi

main "$1"
