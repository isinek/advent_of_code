'''
--- Day 17: Conway Cubes ---
As your flight slowly drifts through the sky, the Elves at the Mythical
Information Bureau at the North Pole contact you. They'd like some help
debugging a malfunctioning experimental energy source aboard one of their
super-secret imaging satellites.

The experimental energy source is based on cutting-edge technology: a set of
Conway Cubes contained in a pocket dimension! When you hear it's having
problems, you can't help but agree to take a look.

The pocket dimension contains an infinite 3-dimensional grid. At every integer
3-dimensional coordinate (x,y,z), there exists a single cube which is either
active or inactive.

In the initial state of the pocket dimension, almost all cubes start inactive.
The only exception to this is a small flat region of cubes (your puzzle input);
the cubes in this region start in the specified active (#) or inactive (.)
state.

The energy source then proceeds to boot up by executing six cycles.

Each cube only ever considers its neighbors: any of the 26 other cubes where any
of their coordinates differ by at most 1. For example, given the cube at
x=1,y=2,z=3, its neighbors include the cube at x=2,y=2,z=2, the cube at
x=0,y=2,z=3, and so on.

During a cycle, all cubes simultaneously change their state according to the
following rules:

If a cube is active and exactly 2 or 3 of its neighbors are also active, the
cube remains active. Otherwise, the cube becomes inactive.
If a cube is inactive but exactly 3 of its neighbors are active, the cube
becomes active. Otherwise, the cube remains inactive.
The engineers responsible for this experimental energy source would like you to
simulate the pocket dimension and determine what the configuration of cubes
should be at the end of the six-cycle boot process.

For example, consider the following initial state:

.#.
..#
###
Even though the pocket dimension is 3-dimensional, this initial state represents
a small 2-dimensional slice of it. (In particular, this initial state defines a
3x3x1 region of the 3-dimensional space.)

Simulating a few cycles from this initial state produces the following
configurations, where the result of each cycle is shown layer-by-layer at each
given z coordinate (and the frame of view follows the active cells in each
cycle):

Before any cycles:

z=0
.#.
..#
###


After 1 cycle:

z=-1
#..
..#
.#.

z=0
#.#
.##
.#.

z=1
#..
..#
.#.


After 2 cycles:

z=-2
.....
.....
..#..
.....
.....

z=-1
..#..
.#..#
....#
.#...
.....

z=0
##...
##...
#....
....#
.###.

z=1
..#..
.#..#
....#
.#...
.....

z=2
.....
.....
..#..
.....
.....


After 3 cycles:

z=-2
.......
.......
..##...
..###..
.......
.......
.......

z=-1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=0
...#...
.......
#......
.......
.....##
.##.#..
...#...

z=1
..#....
...#...
#......
.....##
.#...#.
..#.#..
...#...

z=2
.......
.......
..##...
..###..
.......
.......
.......
After the full six-cycle boot process completes, 112 cubes are left in the
active state.

Starting with your given initial configuration, simulate six cycles. How many
cubes are left in the active state after the sixth cycle?
'''
def conway_cubes_cycle(cubes):
	count_active = {}
	for x in cubes:
		for y in cubes[x]:
			for z in cubes[x][y]:
				for i in range(27):
					if i == 13:
						continue

					xx = x + i//9 - 1
					yy = y + i%9//3 - 1
					zz = z + i%3 - 1

					if not xx in count_active:
						count_active[xx] = {}
					if not yy in count_active[xx]:
						count_active[xx][yy] = {}
					if not zz in count_active[xx][yy]:
						count_active[xx][yy][zz] = 0

					count_active[xx][yy][zz] += 1



	new_cubes = {}
	for x in count_active:
		for y in count_active[x]:
			for z in count_active[x][y]:
				if count_active[x][y][z] == 3 or (x in cubes and y in cubes[x] and z in cubes[x][y] and count_active[x][y][z] == 2):
					if not x in new_cubes:
						new_cubes[x] = {}
					if not y in new_cubes[x]:
						new_cubes[x][y] = [z]
					elif not z in new_cubes[x][y]:
						new_cubes[x][y] += [z]

	return new_cubes


def day_17_task_1():
	cubes = {}
	with open('day_17_conway_cubes.in') as f:
		for i, line in enumerate(f.readlines()):
			for j in range(len(line)):
				if line[j] == '#':
					if not i in cubes:
						cubes[i] = {}
					if not j in cubes[i]:
						cubes[i][j] = [0]

	for _ in range(6):
		cubes = conway_cubes_cycle(cubes)

	print(sum([sum([len(cubes[x][y]) for y in cubes[x]]) for x in cubes]))


'''
--- Part Two ---
For some reason, your simulated results don't match what the experimental energy
source engineers expected. Apparently, the pocket dimension actually has four
spatial dimensions, not three.

The pocket dimension contains an infinite 4-dimensional grid. At every integer
4-dimensional coordinate (x,y,z,w), there exists a single cube (really, a
hypercube) which is still either active or inactive.

Each cube only ever considers its neighbors: any of the 80 other cubes where any
of their coordinates differ by at most 1. For example, given the cube at
x=1,y=2,z=3,w=4, its neighbors include the cube at x=2,y=2,z=3,w=3, the cube at
x=0,y=2,z=3,w=4, and so on.

The initial state of the pocket dimension still consists of a small flat region
of cubes. Furthermore, the same rules for cycle updating still apply: during
each cycle, consider the number of active neighbors of each cube.

For example, consider the same initial state as in the example above. Even
though the pocket dimension is 4-dimensional, this initial state represents a
small 2-dimensional slice of it. (In particular, this initial state defines a
3x3x1x1 region of the 4-dimensional space.)

Simulating a few cycles from this initial state produces the following
configurations, where the result of each cycle is shown layer-by-layer at each
given z and w coordinate:

Before any cycles:

z=0, w=0
.#.
..#
###


After 1 cycle:

z=-1, w=-1
#..
..#
.#.

z=0, w=-1
#..
..#
.#.

z=1, w=-1
#..
..#
.#.

z=-1, w=0
#..
..#
.#.

z=0, w=0
#.#
.##
.#.

z=1, w=0
#..
..#
.#.

z=-1, w=1
#..
..#
.#.

z=0, w=1
#..
..#
.#.

z=1, w=1
#..
..#
.#.


After 2 cycles:

z=-2, w=-2
.....
.....
..#..
.....
.....

z=-1, w=-2
.....
.....
.....
.....
.....

z=0, w=-2
###..
##.##
#...#
.#..#
.###.

z=1, w=-2
.....
.....
.....
.....
.....

z=2, w=-2
.....
.....
..#..
.....
.....

z=-2, w=-1
.....
.....
.....
.....
.....

z=-1, w=-1
.....
.....
.....
.....
.....

z=0, w=-1
.....
.....
.....
.....
.....

z=1, w=-1
.....
.....
.....
.....
.....

z=2, w=-1
.....
.....
.....
.....
.....

z=-2, w=0
###..
##.##
#...#
.#..#
.###.

z=-1, w=0
.....
.....
.....
.....
.....

z=0, w=0
.....
.....
.....
.....
.....

z=1, w=0
.....
.....
.....
.....
.....

z=2, w=0
###..
##.##
#...#
.#..#
.###.

z=-2, w=1
.....
.....
.....
.....
.....

z=-1, w=1
.....
.....
.....
.....
.....

z=0, w=1
.....
.....
.....
.....
.....

z=1, w=1
.....
.....
.....
.....
.....

z=2, w=1
.....
.....
.....
.....
.....

z=-2, w=2
.....
.....
..#..
.....
.....

z=-1, w=2
.....
.....
.....
.....
.....

z=0, w=2
###..
##.##
#...#
.#..#
.###.

z=1, w=2
.....
.....
.....
.....
.....

z=2, w=2
.....
.....
..#..
.....
.....
After the full six-cycle boot process completes, 848 cubes are left in the
active state.

Starting with your given initial configuration, simulate six cycles in a
4-dimensional space. How many cubes are left in the active state after the sixth
cycle?
'''
def conway_cubes_cycle_4d(cubes):
	count_active = {}
	for x in cubes:
		for y in cubes[x]:
			for z in cubes[x][y]:
				for w in cubes[x][y][z]:
					for i in range(81):
						if i == 40:
							continue

						xx = x + i//27 - 1
						yy = y + i%27//9 - 1
						zz = z + i%9//3 - 1
						ww = w + i%3 - 1

						if not xx in count_active:
							count_active[xx] = {}
						if not yy in count_active[xx]:
							count_active[xx][yy] = {}
						if not zz in count_active[xx][yy]:
							count_active[xx][yy][zz] = {}
						if not ww in count_active[xx][yy][zz]:
							count_active[xx][yy][zz][ww] = 0

						count_active[xx][yy][zz][ww] += 1


	new_cubes = {}
	for x in count_active:
		for y in count_active[x]:
			for z in count_active[x][y]:
				for w in count_active[x][y][z]:
					if count_active[x][y][z][w] == 3 or (x in cubes and y in cubes[x] and z in cubes[x][y] and w in cubes[x][y][z] and count_active[x][y][z][w] == 2):
						if not x in new_cubes:
							new_cubes[x] = {}
						if not y in new_cubes[x]:
							new_cubes[x][y] = {}
						if not z in new_cubes[x][y]:
							new_cubes[x][y][z] = [w]
						elif not w in new_cubes[x][y][z]:
							new_cubes[x][y][z] += [w]

	return new_cubes


def day_17_task_2():
	cubes = {}
	with open('day_17_conway_cubes.in') as f:
		for i, line in enumerate(f.readlines()):
			for j in range(len(line)):
				if line[j] == '#':
					if not i in cubes:
						cubes[i] = {}
					cubes[i][j] = {0: [0]}

	for _ in range(6):
		cubes = conway_cubes_cycle_4d(cubes)

	print(sum([sum([sum([len(cubes[x][y][z]) for z in cubes[x][y]]) for y in cubes[x]]) for x in cubes]))


if __name__ == '__main__':
	day_17_task_1()
	day_17_task_2()
