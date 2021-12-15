'''
--- Day 13: Transparent Origami ---
You reach another volcanically active part of the cave. It would be nice if you
could do some kind of thermal imaging so you could tell ahead of time which
caves are too hot to safely enter.

Fortunately, the submarine seems to be equipped with a thermal camera! When you
activate it, you are greeted with:

Congratulations on your purchase! To activate this infrared thermal imaging
camera system, please enter the code found on page 1 of the manual.
Apparently, the Elves have never used this feature. To your surprise, you manage
to find the manual; as you go to open it, page 1 falls out. It's a large sheet
of transparent paper! The transparent paper is marked with random dots and
includes instructions on how to fold it up (your puzzle input). For example:
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5

The first section is a list of dots on the transparent paper. 0,0 represents the
top-left coordinate. The first value, x, increases to the right. The second
value, y, increases downward. So, the coordinate 3,0 is to the right of 0,0, and
the coordinate 0,7 is below 0,0. The coordinates in this example form the
following pattern, where # is a dot on the paper and . is an empty, unmarked
position:
...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
...........
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........

Then, there is a list of fold instructions. Each instruction indicates a line on
the transparent paper and wants you to fold the paper up (for horizontal y=...
lines) or left (for vertical x=... lines). In this example, the first fold
instruction is fold along y=7, which designates the line formed by all of the
positions where y is 7 (marked here with -):
...#..#..#.
....#......
...........
#..........
...#....#.#
...........
...........
-----------
...........
...........
.#....#.##.
....#......
......#...#
#..........
#.#........

Because this is a horizontal line, fold the bottom half up. Some of the dots
might end up overlapping after the fold is complete, but dots will never appear
exactly on a fold line. The result of doing this fold looks like this:
#.##..#..#.
#...#......
......#...#
#...#......
.#.#..#.###
...........
...........

Now, only 17 dots are visible.

Notice, for example, the two dots in the bottom left corner before the
transparent paper is folded; after the fold is complete, those dots appear in
the top left corner (at 0,0 and 0,1). Because the paper is transparent, the dot
just below them in the result (at 0,3) remains visible, as it can be seen
through the transparent paper.

Also notice that some dots can end up overlapping; in this case, the dots merge
together and become a single dot.

The second fold instruction is fold along x=5, which indicates this line:
#.##.|#..#.
#...#|.....
.....|#...#
#...#|.....
.#.#.|#.###
.....|.....
.....|.....

Because this is a vertical line, fold left:
#####
#...#
#...#
#...#
#####
.....
.....

The instructions made a square!

The transparent paper is pretty big, so for now, focus on just completing the
first fold. After the first fold in the example above, 17 dots are
visible - dots that end up overlapping after the fold is completed count as a
single dot.

How many dots are visible after completing just the first fold instruction on
your transparent paper?
'''
def day_13_task_1():
	dots = []
	with open('day_13_transparent_origami.in') as f:
		folds_flag = False
		for line in f.readlines():
			line = line.replace('\n', '')
			if len(line) < 2:
				folds_flag = True
			elif not folds_flag:
				x, y = [int(x) for x in line.split(',')]
				dots += [[y, x]]
			else:
				axis, l = line.split()[2].split('=')
				l = int(l)
				q = dots[:]
				dots = []
				while len(q):
					x = q.pop(0)
					if axis == 'x' and x[1] > l:
						x[1] = l - (x[1] - l)
						if not x in dots:
							dots += [x]
					elif axis == 'y' and x[0] > l:
						x[0] = l - (x[0] - l)
						if not x in dots:
							dots += [x]
					elif not x in dots:
						dots += [x]
				break
	print(len(dots))


'''
--- Part Two ---
Finish folding the transparent paper according to the instructions. The manual
says the code is always eight capital letters.

What code do you use to activate the infrared thermal imaging camera system?
'''
def day_13_task_2():
	dots = []
	with open('day_13_transparent_origami.in') as f:
		folds_flag = False
		for line in f.readlines():
			line = line.replace('\n', '')
			if len(line) < 2:
				folds_flag = True
			elif not folds_flag:
				x, y = [int(x) for x in line.split(',')]
				dots += [[y, x]]
			else:
				axis, l = line.split()[2].split('=')
				l = int(l)
				q = dots[:]
				dots = []
				while len(q):
					x = q.pop(0)
					if axis == 'x' and x[1] > l:
						x[1] = l - (x[1] - l)
						if not x in dots:
							dots += [x]
					elif axis == 'y' and x[0] > l:
						x[0] = l - (x[0] - l)
						if not x in dots:
							dots += [x]
					elif not x in dots:
						dots += [x]

	r = max([x[0] for x in dots])
	c = max([x[1] for x in dots])
	print()
	for i in range(r + 1):
		for j in range(c + 1):
			if [i, j] in dots:
				print('#', end='')
			else:
				print(' ', end='')
		print()


if __name__ == '__main__':
	day_13_task_1()
	day_13_task_2()
