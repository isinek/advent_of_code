'''
--- Day 20: Jurassic Jigsaw ---
The high-speed train leaves the forest and quickly carries you south. You can
even see a desert in the distance! Since you have some spare time, you might as
well see if there was anything interesting in the image the Mythical Information
Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually
contains many small images created by the satellite's camera array. The camera
array consists of many cameras; rather than produce a single square image, they
produce many smaller square image tiles that need to be reassembled back into a
single image.

Each camera in the camera array returns a single monochrome image tile with a
random unique ID number. The tiles (your puzzle input) arrived in a random
order.

Worse yet, the camera array appears to be malfunctioning: each image tile has
been rotated and flipped to a random orientation. Your first task is to
reassemble the original image by orienting the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a
border that should line up exactly with its adjacent tiles. All tiles have this
border, and the border lines up exactly when the tiles are both oriented
correctly. Tiles at the edge of the image also have this border, but the
outermost edges won't line up with any other tiles.

For example, suppose you have the following nine tiles:

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...
By rotating, flipping, and rearranging them, you can find a square arrangement
that causes all adjacent borders to line up:

#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....
For reference, the IDs of the above tiles are:

1951    2311    3079
2729    1427    2473
2971    1489    1171
To check that you've assembled the image correctly, multiply the IDs of the four
corner tiles together. If you do this with the assembled tiles from the example
above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

Assemble the tiles into an image. What do you get if you multiply together the
IDs of the four corner tiles?
'''
def day_20_task_1():
	tiles = {}
	with open('day_20_jurassic_jigsaw.in') as f:
		tile_id = None
		for line in f.readlines():
			if len(line) < 5:
				tile_id = None
			elif tile_id is None:
				tile_id = int(line.strip('\n').split()[1][:-1])
				tiles[tile_id] = {'tiles': [], 'L': None, 'R': None, 'U': None, 'D': None}
			else:
				tiles[tile_id]['tiles'] += [line.strip('\n')]
	tile_ids = sorted(list(tiles.keys()))
	for i, id_1 in enumerate(tile_ids[:-1]):
		for id_2 in tile_ids[i + 1:]:
			if id_1 == id_2:
				continue

			match = [True for _ in range(32)]
			for k in range(len(tiles[id_1]['tiles'])):
				#	 UP      UP FLIPPED   DOWN     DOWN FLIPPED LEFT    LEFT FLIPPED RIGHT    RIGHT FLIPPED
				sides = [(0, k), (0, -1 - k), (-1, k), (-1, -1 -k), (k, 0), (-1 - k, 0), (k, -1), (-1 - k, -1)]
				for l in range(32):
					if match[l] and tiles[id_1]['tiles'][sides[l//8*2][0]][sides[l//8*2][1]] != tiles[id_2]['tiles'][sides[l%8][0]][sides[l%8][1]]:
						match[l] = False
				if not any(match):
					break

			sides = ['U', 'D', 'L', 'R']
			for k in range(32):
				if match[k]:
					tiles[id_1][sides[k//8]] = id_2
					tiles[id_2][sides[k%8//2]] = id_1
					break

	res = 1
	for x in tiles:
		s = sum([[0, 1][tiles[x][d] is None] for d in tiles[x]])
		if s == 2:
			res *= x
	print(res)


'''
--- Part Two ---
Now, you're ready to check the image for sea monsters.

The borders of each tile are not part of the actual image; start by removing
them.

In the example above, the tiles become:

.#.#..#. ##...#.# #..#####
###....# .#....#. .#......
##.##.## #.#.#..# #####...
###.#### #...#.## ###.#..#
##.#.... #.##.### #...#.##
...##### ###.#... .#####.#
....#..# ...##..# .#.###..
.####... #..#.... .#......

#..#.##. .#..###. #.##....
#.####.. #.####.# .#.###..
###.#.#. ..#.#### ##.#..##
#.####.. ..##..## ######.#
##..##.# ...#...# .#.#.#..
...#..#. .#.#.##. .###.###
.#.#.... #.##.#.. .###.##.
###.#... #..#.##. ######..

.#.#.### .##.##.# ..#.##..
.####.## #.#...## #.#..#.#
..#.#..# ..#.#.#. ####.###
#..####. ..#.#.#. ###.###.
#####..# ####...# ##....##
#.##..#. .#...#.. ####...#
.#.###.. ##..##.. ####.##.
...###.. .##...#. ..#..###
Remove the gaps to form the actual image:

.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###
Now, you're ready to search for sea monsters! Because your image is monochrome,
a sea monster will look like this:

                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
When looking for this pattern in the image, the spaces can be anything; only the
# need to match. Also, you might need to rotate or flip your image before it's
# oriented correctly to find sea monsters. In the above image, after flipping
# and rotating it to the appropriate orientation, there are two sea monsters
# (marked with O):

.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#
Determine how rough the waters are in the sea monsters' habitat by counting the
number of # that are not part of a sea monster. In the above example, the
habitat's water roughness is 273.

How many # are not part of a sea monster?
'''
def rotate_tile(tile, curr_orient, right_orient, connection):
	sides = ['U', 'D', 'L', 'R']
	curr_orient = sides.index(curr_orient)
	right_orient = sides.index(right_orient)

	rotated = tile['tiles'][:]
	if curr_orient != right_orient and curr_orient//2 == right_orient//2:
		for i in range(len(rotated)//2):
			rotated[i], rotated[-i - 1] = rotated[-i - 1][::-1], rotated[i][::-1]
		tile['U'], tile['D'], tile['L'], tile['R'] = tile['D'], tile['U'], tile['R'], tile['L']
	elif (curr_orient == 0 and right_orient == 2) or (curr_orient == 1 and right_orient == 3) or (curr_orient == 2 and right_orient == 1) or (curr_orient == 3 and right_orient == 0):
		tmp = []
		width = len(rotated[0])
		for j in range(width):
			tmp += ['']
			for i in range(len(rotated)):
				tmp[-1] += rotated[i][width - 1 - j]
		rotated = tmp
		tile['U'], tile['D'], tile['L'], tile['R'] = tile['R'], tile['L'], tile['U'], tile['D']
	elif (curr_orient == 0 and right_orient == 3) or (curr_orient == 1 and right_orient == 2) or (curr_orient == 2 and right_orient == 0) or (curr_orient == 3 and right_orient == 1):
		tmp = []
		height = len(rotated)
		for j in range(len(rotated[0])):
			tmp += ['']
			for i in range(height):
				tmp[-1] += rotated[height - 1 - i][j]
		rotated = tmp
		tile['U'], tile['D'], tile['L'], tile['R'] = tile['L'], tile['R'], tile['D'], tile['U']

	if sides[right_orient] == 'U' and rotated[0] != connection:
		for i in range(len(rotated)):
			rotated[i] = rotated[i][::-1]
		tile['L'], tile['R'] = tile['R'], tile['L']
	elif sides[right_orient] == 'L' and ''.join([row[0] for row in rotated]) != connection:
		for i in range(len(rotated)//2):
			rotated[i], rotated[-i - 1] = rotated[-i - 1], rotated[i]
		tile['U'], tile['D'] = tile['D'], tile['U']

	tile['tiles'] = rotated


def day_20_task_2():
	tiles = {}
	with open('day_20_jurassic_jigsaw.in') as f:
		tile_id = None
		for line in f.readlines():
			if len(line) < 5:
				tile_id = None
			elif tile_id is None:
				tile_id = int(line.strip('\n').split()[1][:-1])
				tiles[tile_id] = {'tiles': [], 'L': None, 'R': None, 'U': None, 'D': None}
			else:
				tiles[tile_id]['tiles'] += [line.strip('\n')]
	tile_ids = sorted(list(tiles.keys()))
	for i, id_1 in enumerate(tile_ids[:-1]):
		for id_2 in tile_ids[i + 1:]:
			if id_1 == id_2:
				continue

			match = [True for _ in range(32)]
			for k in range(len(tiles[id_1]['tiles'])):
				#	 UP      UP FLIPPED   DOWN         DOWN F.  LEFT         LEFT F. RIGHT    RIGHT FLIPPED
				sides = [(0, k), (0, -1 - k), (-1, -1 -k), (-1, k), (-1 - k, 0), (k, 0), (k, -1), (-1 - k, -1)]
				for l in range(32):
					if match[l] and tiles[id_1]['tiles'][sides[l//8*2][0]][sides[l//8*2][1]] != tiles[id_2]['tiles'][sides[l%8][0]][sides[l%8][1]]:
						match[l] = False
				if not any(match):
					break

			sides = ['U', 'D', 'L', 'R']
			for k in range(32):
				if match[k]:
					tiles[id_1][sides[k//8]] = id_2
					tiles[id_2][sides[k%8//2]] = id_1
					break

	tile_queue = [[x for x in tile_ids if tiles[x]['L'] is None and tiles[x]['U'] is None][0]]
	sides = ['U', 'D', 'L', 'R']
	while len(tile_queue):
		x = tile_queue.pop(0)
		if not tiles[x]['D'] is None:
			d = tiles[x]['D']
			x_orient = 'U'
			for s in sides:
				if tiles[d][s] == x:
					x_orient = s
					break
			rotate_tile(tiles[d], x_orient, 'U', tiles[x]['tiles'][-1])

			if not d in tile_queue:
				tile_queue.append(d)
		if not tiles[x]['R'] is None:
			r = tiles[x]['R']
			x_orient = 'L'
			for s in sides:
				if tiles[r][s] == x:
					x_orient = s
					break
			rotate_tile(tiles[r], x_orient, 'L', ''.join([row[-1] for row in tiles[x]['tiles']]))

			if not r in tile_queue:
				tile_queue.append(r)

	image = []
	ids = {'R': [], 'D': []}
	for x in tiles:
		if tiles[x]['L'] is None and tiles[x]['U'] is None:
			ids['D'] += [x]

	x = -len(tiles[ids['D'][0]]['tiles'])
	while (len(ids['R']) or len(ids['D'])):
		if len(ids['R']):
			i = ids['R'].pop(0)
		else:
			i = ids['D'].pop(0)
			image += [[] for _ in range(len(tiles[i]['tiles']))]
			x += len(tiles[i]['tiles'])

		for j, r in enumerate(tiles[i]['tiles'][1:-1]):
			image[x + j] += [''.join(r[1:-1])]

		if not len(ids['D']) and not tiles[i]['D'] is None:
			ids['D'] += [tiles[i]['D']]
		if not tiles[i]['R'] is None:
			ids['R'] += [tiles[i]['R']]

	i = 0
	roughness = 0
	while i < len(image):
		if not len(image[i]):
			image.pop(i)
		else:
			image[i] = ''.join(image[i])
			roughness += sum(1 for y in image[i] if y == '#')
			i += 1

	monster_image = ['                  O ', 'O    OO    OO    OOO', ' O  O  O  O  O  O   ']
	monsters = [[] for _ in range(8)]
	for i, x in enumerate(monster_image):
		for j, y in enumerate(x):
			if y == 'O':
				monsters[0] += [(i, j)]
				monsters[1] += [(i, len(x) - 1 - j)]
				monsters[2] += [(len(monster_image) - 1 - i, j)]
				monsters[3] += [(len(monster_image) - 1 - i, len(x) - 1 - j)]
				monsters[4] += [(j, i)]
				monsters[5] += [(len(x) - 1 - j, i)]
				monsters[6] += [(j, len(monster_image) - 1 - i)]
				monsters[7] += [(len(x) - 1 - j, len(monster_image) - 1 - i)]

	max_rm = 0
	for m in monsters:
		rm = 0
		max_x = max([x[0] for x in m])
		max_y = max([x[1] for x in m])
		for i in range(len(image) - max_x):
			for j in range(len(image[i]) - max_y):
				if all([[False, True][image[x[0] + i][x[1] + j] == '#'] for x in m]):
					rm += 1
		if rm > max_rm:
			max_rm = rm

	print(roughness - max_rm*len(monsters[0]))


if __name__ == '__main__':
	# day_20_task_1()
	day_20_task_2()
