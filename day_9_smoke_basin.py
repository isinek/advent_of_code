'''
--- Day 9: Smoke Basin ---
These caves seem to be lava tubes. Parts are even still volcanically active;
small hydrothermal vents release smoke into the caves that slowly settles like
rain.

If you can model how the smoke flows through the caves, you might be able to
avoid it and be that much safer. The submarine generates a heightmap of the
floor of the nearby caves for you (your puzzle input).

Smoke flows to the lowest point of the area it's in. For example, consider the
following heightmap:

2199943210
3987894921
9856789892
8767896789
9899965678

Each number corresponds to the height of a particular location, where 9 is the
highest and 0 is the lowest a location can be.

Your first goal is to find the low points - the locations that are lower than
any of its adjacent locations. Most locations have four adjacent locations (up,
down, left, and right); locations on the edge or corner of the map have three or
two adjacent locations, respectively. (Diagonal locations do not count as
adjacent.)

In the above example, there are four low points, all highlighted: two are in the
first row (a 1 and a 0), one is in the third row (a 5), and one is in the bottom
row (also a 5). All other locations on the heightmap have some lower adjacent
location, and so are not low points.

The risk level of a low point is 1 plus its height. In the above example, the
risk levels of the low points are 2, 1, 6, and 6. The sum of the risk levels of
all low points in the heightmap is therefore 15.

Find all of the low points on your heightmap. What is the sum of the risk levels
of all low points on your heightmap?
'''
def day_9_task_1():
	risk = 0
	nums = []
	with open('day_9_smoke_basin.in') as f:
		for line in f.readlines():
			nums += [[int(x) for x in line.replace('\n', '')]]

	for i in range(len(nums)):
		for j in range(len(nums[i])):
			x = 0
			if i == 0 or nums[i - 1][j] > nums[i][j]:
				x += 1
			if i == len(nums) - 1 or nums[i + 1][j] > nums[i][j]:
				x += 1
			if j == 0 or nums[i][j - 1] > nums[i][j]:
				x += 1
			if j == len(nums[i]) - 1 or nums[i][j + 1] > nums[i][j]:
				x += 1

			if x == 4:
				risk += nums[i][j] + 1
	print(risk)


'''
--- Part Two ---
Next, you need to find the largest basins so you know what areas are most
important to avoid.

A basin is all locations that eventually flow downward to a single low point.
Therefore, every low point has a basin, although some basins are very small.
Locations of height 9 do not count as being in any basin, and all other
locations will always be part of exactly one basin.

The size of a basin is the number of locations within the basin, including the
low point. The example above has four basins.

The top-left basin, size 3:
2199943210
3987894921
9856789892
8767896789
9899965678

The top-right basin, size 9:
2199943210
3987894921
9856789892
8767896789
9899965678

The middle basin, size 14:
2199943210
3987894921
9856789892
8767896789
9899965678

The bottom-right basin, size 9:
2199943210
3987894921
9856789892
8767896789
9899965678

Find the three largest basins and multiply their sizes together. In the above
example, this is 9 * 14 * 9 = 1134.

What do you get if you multiply together the sizes of the three largest basins?
'''
def day_9_task_2():
	basins = []
	nums = []
	with open('day_9_smoke_basin.in') as f:
		for line in f.readlines():
			nums += [[int(x) for x in line.replace('\n', '')]]

	for i in range(len(nums)):
		for j in range(len(nums[i])):
			x = 0
			if i == 0 or nums[i - 1][j] > nums[i][j]:
				x += 1
			if i == len(nums) - 1 or nums[i + 1][j] > nums[i][j]:
				x += 1
			if j == 0 or nums[i][j - 1] > nums[i][j]:
				x += 1
			if j == len(nums[i]) - 1 or nums[i][j + 1] > nums[i][j]:
				x += 1

			if x == 4:
				basins += [0]
				flood = [(i, j)]
				b = []
				while len(flood):
					x, y = flood.pop()
					b += [(i, j)]
					basins[-1] += 1
					if x - 1 >= 0 and nums[x - 1][y] < 9 and not (x - 1, y) in b:
						flood += [(x - 1, y)]
						b += [(x - 1, y)]
					if x + 1 < len(nums) and nums[x + 1][y] < 9 and not (x + 1, y) in b:
						flood += [(x + 1, y)]
						b += [(x + 1, y)]
					if y - 1 >= 0 and nums[x][y - 1] < 9 and not (x, y - 1) in b:
						flood += [(x, y - 1)]
						b += [(x, y - 1)]
					if y + 1 < len(nums[i]) and nums[x][y + 1] < 9 and not (x, y + 1) in b:
						flood += [(x, y + 1)]
						b += [(x, y + 1)]

	basins = sorted(basins, key=lambda x: -x)
	print(basins[0]*basins[1]*basins[2])


if __name__ == '__main__':
	day_9_task_1()
	day_9_task_2()
