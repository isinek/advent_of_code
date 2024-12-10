#!/bin/bash

# --- Part Two ---
# Upon completion, two things immediately become clear. First, the disk
# definitely has a lot more contiguous free space, just like the amphipod hoped.
# Second, the computer is running much more slowly! Maybe introducing all of
# that file system fragmentation was a bad idea?
# 
# The eager amphipod already has a new plan: rather than move individual blocks,
# he'd like to try compacting the files on his disk by moving whole files
# instead.
# 
# This time, attempt to move whole files to the leftmost span of free space
# blocks that could fit the file. Attempt to move each file exactly once in
# order of decreasing file ID number starting with the file with the highest
# file ID number. If there is no span of free space to the left of a file that
# is large enough to fit the file, the file does not move.
# 
# The first example from above now proceeds differently:
# 00...111...2...333.44.5555.6666.777.888899
# 0099.111...2...333.44.5555.6666.777.8888..
# 0099.1117772...333.44.5555.6666.....8888..
# 0099.111777244.333....5555.6666.....8888..
# 00992111777.44.333....5555.6666.....8888..
# 
# The process of updating the filesystem checksum is the same; now, this
# example's checksum would be 2858.
# 
# Start over, now compacting the amphipod's hard drive using this new method
# instead. What is the resulting filesystem checksum?

function main() {
  local input_file="$1"
  local p=0
  local id=0
  local li=0

  while [ "${li}" -ge 0 ]; do
    local i=0

    line="$( cut -c $(( li*1024 + 1 ))-$(( (li + 1)*1024 )) < "${input_file}" )"
    if [ -z "${line}" ]; then
      break
    fi

    touch blocks.tmp
    touch free_blocks.tmp

    while [ "${i}" -lt "${#line}" ]; do
      local size="${line:${i}:1}"
      local free_space="${line:$(( i + 1 )):1}"

      echo "${p} ${size} ${id}" >> blocks.tmp
      if [ -n "${free_space}" ] && [ "${free_space}" -gt 0 ]; then
        echo "$(( p + size )) ${free_space}" >> free_blocks.tmp
      fi
      p=$(( p + size + free_space ))
      (( id++ ))
      i=$(( i + 2 ))
    done

    (( li++ ))
  done

  sort -n -r -k 1 -o blocks.tmp blocks.tmp

  touch new_blocks.tmp
  while read -r pos size id; do
    local free_block=

    read -r -a free_block < <( awk -F' ' "{ if ( \$1 < ${pos} && \$2 >= ${size} ) print \$0 }" free_blocks.tmp | head -1 )
    if [ -z "${free_block[*]}" ]; then
      echo "${pos} ${size} ${id}" >> new_blocks.tmp
      continue
    fi

    echo "${free_block[0]} ${size} ${id}" >> new_blocks.tmp

    sed -i 's/^'"${free_block[*]}"'$/'"$(( free_block[0] + size ))"' '"$(( free_block[1] - size ))"'/' free_blocks.tmp
  done < blocks.tmp

  local sum=0
  while read -r pos size id; do
    for i in $( seq "${pos}" $(( pos + size - 1 )) ); do
      sum=$(( sum + i*id ))
    done
  done < new_blocks.tmp

  echo "${sum}"
  rm -f blocks.tmp free_blocks.tmp new_blocks.tmp
}

if [ $# -ne 1 ]; then
  echo "$0 <task_data.in>"
  exit 1
fi

main "$1"
