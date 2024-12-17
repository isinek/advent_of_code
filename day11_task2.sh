#!/bin/bash

# --- Part Two ---
# The Historians sure are taking a long time. To be fair, the infinite corridors
# are very large.
# 
# How many stones would you have after blinking a total of 75 times?

function blink() {
  if [ "$1" -eq 0 ]; then
    echo "1"
  elif [ "$(( ${#1}%2 ))" -eq 0 ]; then
    echo "${1:0:$(( ${#1}/2 ))}"
    echo "$(( 10#${1:$(( ${#1}/2 ))} ))"
  else
    echo "$(( $1*2024 ))"
  fi
}

function main() {
  local input_file="$1"
  local -i base_stones=()
  local blink=75
  local stones_q=()

  read -r -a base_stones < "${input_file}"

  for s in "${base_stones[@]}"; do
    stones_q=( "${stones_q[@]}" "${s}_${blink}" )
  done

  while [ "${#stones_q[@]}" -gt 0 ]; do
    local s="${stones_q[0]%_*}"
    local b="${stones_q[0]#*_}"
    local sfile="stones_${s}_${b}.tmp"

    stones_q=( "${stones_q[@]:1}" )

    if [ -f "${sfile}" ]; then
      continue
    elif [ "${b}" -eq 1 ]; then
      local stones=()
      mapfile -t stones < <( blink "${s}" )

      touch "${sfile}"
      echo "${#stones[@]}" > "${sfile}"
      continue
    fi

    local stones=()
    mapfile -t stones < <( blink "${s}" )

    touch "${sfile}"
    for ss in "${stones[@]}"; do
      echo "stones_${ss}_$(( b - 1 )).tmp" >> "${sfile}"
      stones_q=( "${ss}_$(( b - 1 ))" "${stones_q[@]}" )
    done
  done

  for i in $( seq 1 "$(( blink - 1 ))" ); do
    echo "level: ${i}"
    local sfiles=( $( ls stones_*_${i}.tmp ) )

    for sfile in "${sfiles[@]}"; do
      local sum=0
      sum="$( awk 'BEGIN { sum = 0 }; { sum += $1 }; END { print sum }' "${sfile}" )"
      echo "${sum}" > "${sfile}"

      while read -r gsf; do
        sed -i "s/${sfile}/${sum}/g" "${gsf%:*}"
      done < <( grep "${sfile}" *_$(( i + 1 )).tmp )
    done

    rm -f "${sfiles[@]}"
  done

  cat stones_*_${blink}.tmp | awk 'BEGIN { sum = 0 }; { sum += $1 }; END { print sum }'
}

if [ $# -ne 1 ]; then
  echo "$0 <task_data.in>"
  exit 1
fi

main "$1"
