#!/bin/bash

# --- Day 9: Disk Fragmenter ---
# Another push of the button leaves you in the familiar hallways of some
# friendly amphipods! Good thing you each somehow got your own personal mini
# submarine. The Historians jet away in search of the Chief, mostly by driving
# directly into walls.
# 
# While The Historians quickly figure out how to pilot these things, you notice
# an amphipod in the corner struggling with his computer. He's trying to make
# more contiguous free space by compacting all of the files, but his program
# isn't working; you offer to help.
# 
# He shows you the disk map (your puzzle input) he's already generated. For
# example:
# 2333133121414131402
# 
# The disk map uses a dense format to represent the layout of files and free
# space on the disk. The digits alternate between indicating the length of a
# file and the length of free space.
# 
# So, a disk map like 12345 would represent a one-block file, two blocks of free
# space, a three-block file, four blocks of free space, and then a five-block
# file. A disk map like 90909 would represent three nine-block files in a row
# (with no free space between them).
# 
# Each file on disk also has an ID number based on the order of the files as
# they appear before they are rearranged, starting with ID 0. So, the disk map
# 12345 has three files: a one-block file with ID 0, a three-block file with ID
# 1, and a five-block file with ID 2. Using one character for each block where
# digits are the file ID and . is free space, the disk map 12345 represents
# these individual blocks:
# 0..111....22222
# 
# The first example above, 2333133121414131402, represents these individual
# blocks:
# 00...111...2...333.44.5555.6666.777.888899
# 
# The amphipod would like to move file blocks one at a time from the end of the
# disk to the leftmost free space block (until there are no gaps remaining
# between file blocks). For the disk map 12345, the process looks like this:
# 0..111....22222
# 02.111....2222.
# 022111....222..
# 0221112...22...
# 02211122..2....
# 022111222......
# 
# The first example requires a few more steps:
# 00...111...2...333.44.5555.6666.777.888899
# 009..111...2...333.44.5555.6666.777.88889.
# 0099.111...2...333.44.5555.6666.777.8888..
# 00998111...2...333.44.5555.6666.777.888...
# 009981118..2...333.44.5555.6666.777.88....
# 0099811188.2...333.44.5555.6666.777.8.....
# 009981118882...333.44.5555.6666.777.......
# 0099811188827..333.44.5555.6666.77........
# 00998111888277.333.44.5555.6666.7.........
# 009981118882777333.44.5555.6666...........
# 009981118882777333644.5555.666............
# 00998111888277733364465555.66.............
# 0099811188827773336446555566..............
# 
# The final step of this file-compacting process is to update the filesystem
# checksum. To calculate the checksum, add up the result of multiplying each of
# these blocks' position with the file ID number it contains. The leftmost block
# is in position 0. If a block contains free space, skip it instead.
# 
# Continuing the first example, the first few blocks' position multiplied by its
# file ID number are 0 * 0 = 0, 1 * 0 = 0, 2 * 9 = 18, 3 * 9 = 27, 4 * 8 = 32,
# and so on. In this example, the checksum is the sum of these, 1928.
# 
# Compact the amphipod's hard drive using the process he requested. What is the
# resulting filesystem checksum? (Be careful copy/pasting the input for this
# puzzle; it is a single, very long line.)

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

    wc -l blocks.tmp free_blocks.tmp

    (( li++ ))
  done

  mapfile -t block_q < <( cat blocks.tmp | sort -n -r -k 1 )
  mapfile -t free_block_q < <( cat free_blocks.tmp | sort -n -k 1)

  local cur_block=( ${block_q[0]} )
  local cur_free_block=( ${free_block_q[0]} )
  block_q=( "${block_q[@]:1}" )
  free_block_q=( "${free_block_q[@]:1}" )
  while [ "${cur_block[0]}" -gt "${cur_free_block[0]}" ]; do
    if [ "${cur_block[1]}" -ge "${cur_free_block[1]}" ]; then
      block_q=( "${block_q[@]}" "${cur_free_block[0]} ${cur_free_block[1]} ${cur_block[2]}" )
      cur_block[1]=$(( cur_block[1] - cur_free_block[1] ))
      cur_free_block[1]=0
    else
      block_q=( "${block_q[@]}" "${cur_free_block[0]} ${cur_block[1]} ${cur_block[2]}" )
      cur_free_block[0]=$(( cur_free_block[0] + cur_block[1] ))
      cur_free_block[1]=$(( cur_free_block[1] - cur_block[1] ))
      cur_block[1]=0
    fi

    if [ "${cur_block[1]}" -eq 0 ]; then
      cur_block=( ${block_q[0]} )
      block_q=( "${block_q[@]:1}" )
    fi

    if [ "${cur_free_block[1]}" -eq 0 ]; then
      cur_free_block=( ${free_block_q[0]} )
      free_block_q=( "${free_block_q[@]:1}" )
    fi
  done

  printf "%s\n" "${block_q[@]}" "${cur_block[*]}" | sort -n -k 1

  local sum=0
  for x in "${block_q[@]}" "${cur_block[*]}"; do
    local block=( ${x} )

    for i in $( seq "${block[0]}" $(( block[0] + block[1] - 1 )) ); do
      sum=$(( sum + i*block[2] ))
    done
  done

  echo "${sum}"
  rm -f blocks.tmp free_blocks.tmp
}

if [ $# -ne 1 ]; then
  echo "$0 <task_data.in>"
  exit 1
fi

main "$1"
