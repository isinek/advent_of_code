'''
--- Day 24: Lobby Layout ---
Your raft makes it to the tropical island; it turns out that the small crab was
an excellent navigator. You make your way to the resort.

As you enter the lobby, you discover a small problem: the floor is being
renovated. You can't even reach the check-in desk until they've finished
installing the new tile floor.

The tiles are all hexagonal; they need to be arranged in a hex grid with a very
specific color pattern. Not in the mood to wait, you offer to help figure out
the pattern.

The tiles are all white on one side and black on the other. They start with the
white side facing up. The lobby is large enough to fit whatever pattern might
need to appear there.

A member of the renovation crew gives you a list of the tiles that need to be
flipped over (your puzzle input). Each line in the list identifies a single tile
that needs to be flipped by giving a series of steps starting from a reference
tile in the very center of the room. (Every line starts from the same reference
tile.)

Because the tiles are hexagonal, every tile has six neighbors: east, southeast,
southwest, west, northwest, and northeast. These directions are given in your
list, respectively, as e, se, sw, w, nw, and ne. A tile is identified by a
series of these directions with no delimiters; for example, esenee identifies
the tile you land on if you start at the reference tile and then move one tile
east, one tile southeast, one tile northeast, and one tile east.

Each time a tile is identified, it flips from white to black or from black to
white. Tiles might be flipped more than once. For example, a line like esew
flips a tile immediately adjacent to the reference tile, and a line like nwwswee
flips the reference tile itself.

Here is a larger example:

sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew
In the above example, 10 tiles are flipped once (to black), and 5 more are
flipped twice (to black, then back to white). After all of these instructions
have been followed, a total of 10 tiles are black.

Go through the renovation crew's list and determine which tiles they need to
flip. After all of the instructions have been followed, how many tiles are left
with the black side up?
'''
def day_24_task_1():
	with open('day_24_lobby_layout.in') as f:
		black_tiles = []
		for line in f.readlines():
			coord = [0, 0]
			i = 0
			while i < len(line.strip('\n')):
				x = 1
				if line[i] in ['s', 'n']:
					coord[1] += [-1, 1][line[i] == 'n']
					x = 0.5
					i += 1

				if line[i] == 'e':
					coord[0] -= x
				elif line[i] == 'w':
					coord[0] += x
				i += 1

			x = tuple(coord)
			if x in black_tiles:
				black_tiles.remove(x)
			else:
				black_tiles += [x]

	print(len(black_tiles))


'''
--- Part Two ---
The tile floor in the lobby is meant to be a living art exhibit. Every day, the
tiles are all flipped according to the following rules:

Any black tile with zero or more than 2 black tiles immediately adjacent to it
is flipped to white.
Any white tile with exactly 2 black tiles immediately adjacent to it is flipped
to black.
Here, tiles immediately adjacent means the six tiles directly touching the tile
in question.

The rules are applied simultaneously to every tile; put another way, it is first
determined which tiles need to be flipped, then they are all flipped at the same
time.

In the above example, the number of black tiles that are facing up after the
given number of days has passed is as follows:

Day 1: 15
Day 2: 12
Day 3: 25
Day 4: 14
Day 5: 23
Day 6: 28
Day 7: 41
Day 8: 37
Day 9: 49
Day 10: 37

Day 20: 132
Day 30: 259
Day 40: 406
Day 50: 566
Day 60: 788
Day 70: 1106
Day 80: 1373
Day 90: 1844
Day 100: 2208
After executing this process a total of 100 times, there would be 2208 black
tiles facing up.

How many tiles will be black after 100 days?
'''
def day_24_task_2():
	with open('day_24_lobby_layout.in') as f:
		black_tiles = []
		for line in f.readlines():
			coord = [0, 0]
			i = 0
			while i < len(line.strip('\n')):
				x = 1
				if line[i] in ['s', 'n']:
					coord[1] += [-1, 1][line[i] == 'n']
					x = 0.5
					i += 1

				if line[i] == 'e':
					coord[0] -= x
				elif line[i] == 'w':
					coord[0] += x
				i += 1

			x = tuple(coord)
			if x in black_tiles:
				black_tiles.remove(x)
			else:
				black_tiles += [x]

	adjacent_tiles = [(-1, 0), (-0.5, -1), (0.5, -1), (1, 0), (0.5, 1), (-0.5, 1)]
	for i in range(1, 101):
		flip_tiles = []
		for x in black_tiles:
			count = sum([1 for y in adjacent_tiles if (x[0] + y[0], x[1] + y[1]) in black_tiles])
			if count == 0 or count > 2:
				flip_tiles += [x]

			for yy in adjacent_tiles:
				xx = (x[0] + yy[0], x[1] + yy[1])
				if xx in flip_tiles or xx in black_tiles:
					continue

				count = sum([1 for y in adjacent_tiles if (xx[0] + y[0], xx[1] + y[1]) in black_tiles])
				if count == 2:
					flip_tiles += [xx]

		for x in flip_tiles:
			if x in black_tiles:
				black_tiles.remove(x)
			else:
				black_tiles += [x]

	print(len(black_tiles))


if __name__ == '__main__':
	day_24_task_1()
	day_24_task_2()
