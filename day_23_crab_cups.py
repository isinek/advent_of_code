'''
--- Day 23: Crab Cups ---
The small crab challenges you to a game! The crab is going to mix up some cups,
and you have to predict where they'll end up.

The cups will be arranged in a circle and labeled clockwise (your puzzle input).
For example, if your labeling were 32415, there would be five cups in the
circle; going clockwise around the circle from the first cup, the cups would be
labeled 3, 2, 4, 1, 5, and then back to 3 again.

Before the crab starts, it will designate the first cup in your list as the
current cup. The crab is then going to do 100 moves.

Each move, the crab does the following actions:

The crab picks up the three cups that are immediately clockwise of the current
cup. They are removed from the circle; cup spacing is adjusted as necessary to
maintain the circle.
The crab selects a destination cup: the cup with a label equal to the current
cup's label minus one. If this would select one of the cups that was just picked
up, the crab will keep subtracting one until it finds a cup that wasn't just
picked up. If at any point in this process the value goes below the lowest value
on any cup's label, it wraps around to the highest value on any cup's label
instead.
The crab places the cups it just picked up so that they are immediately
clockwise of the destination cup. They keep the same order as when they were
picked up.
The crab selects a new current cup: the cup which is immediately clockwise of
the current cup.
For example, suppose your cup labeling were 389125467. If the crab were to do
merely 10 moves, the following changes would occur:

-- move 1 --
cups: (3) 8  9  1  2  5  4  6  7 
pick up: 8, 9, 1
destination: 2

-- move 2 --
cups:  3 (2) 8  9  1  5  4  6  7 
pick up: 8, 9, 1
destination: 7

-- move 3 --
cups:  3  2 (5) 4  6  7  8  9  1 
pick up: 4, 6, 7
destination: 3

-- move 4 --
cups:  7  2  5 (8) 9  1  3  4  6 
pick up: 9, 1, 3
destination: 7

-- move 5 --
cups:  3  2  5  8 (4) 6  7  9  1 
pick up: 6, 7, 9
destination: 3

-- move 6 --
cups:  9  2  5  8  4 (1) 3  6  7 
pick up: 3, 6, 7
destination: 9

-- move 7 --
cups:  7  2  5  8  4  1 (9) 3  6 
pick up: 3, 6, 7
destination: 8

-- move 8 --
cups:  8  3  6  7  4  1  9 (2) 5 
pick up: 5, 8, 3
destination: 1

-- move 9 --
cups:  7  4  1  5  8  3  9  2 (6)
pick up: 7, 4, 1
destination: 5

-- move 10 --
cups: (5) 7  4  1  8  3  9  2  6 
pick up: 7, 4, 1
destination: 3

-- final --
cups:  5 (8) 3  7  4  1  9  2  6 
In the above example, the cups' values are the labels as they appear moving
clockwise around the circle; the current cup is marked with ( ).

After the crab is done, what order will the cups be in? Starting after the cup
labeled 1, collect the other cups' labels clockwise into a single string with no
extra characters; each number except 1 should appear exactly once. In the above
example, after 10 moves, the cups clockwise from 1 are labeled 9, 2, 6, 5, and
so on, producing 92658374. If the crab were to complete all 100 moves, the order
after cup 1 would be 67384529.

Using your labeling, simulate 100 moves. What are the labels on the cups after
cup 1?

Your puzzle input is 685974213.
'''
def day_23_task_1():
	cups = [int(x) for x in '389125467']

	for _ in range(100):
		first = cups.pop(0)
		for_insert = [cups.pop(0) for _ in [0]*3]

		destination_val = first - 1
		if destination_val == 0:
			destination_val = 9

		for _ in [0]*3:
			if destination_val in for_insert:
				destination_val -= 1
				if destination_val == 0:
					destination_val = 9
		destination = cups.index(destination_val)
		for x in for_insert[::-1]:
			cups.insert(destination + 1, x)
		cups += [first]

	i = cups.index(1)
	print(''.join([str(x) for x in cups[i + 1:] + cups[:i]]))


'''
--- Part Two ---
Due to what you can only assume is a mistranslation (you're not exactly fluent
in Crab), you are quite surprised when the crab starts arranging many cups in a
circle on your raft - one million (1000000) in total.

Your labeling is still correct for the first few cups; after that, the remaining
cups are just numbered in an increasing fashion starting from the number after
the highest number in your list and proceeding one by one until one million is
reached. (For example, if your labeling were 54321, the cups would be numbered
5, 4, 3, 2, 1, and then start counting up from 6 until one million is reached.)
In this way, every number from one through one million is used exactly once.

After discovering where you made the mistake in translating Crab Numbers, you
realize the small crab isn't going to do merely 100 moves; the crab is going to
do ten million (10000000) moves!

The crab is going to hide your stars - one each - under the two cups that will
end up immediately clockwise of cup 1. You can have them if you predict what the
labels on those cups will be when the crab is finished.

In the above example (389125467), this would be 934001 and then 159792;
multiplying these together produces 149245887792.

Determine which two cups will end up immediately clockwise of cup 1. What do you
get if you multiply their labels together?
'''
def day_23_task_2():
	init = '685974213'
	cups = {}
	for i, x in enumerate(init):
		cups[int(x)] = {'prev': int(init[i - 1]), 'next': int(init[(i + 1)%len(init)])}
	for i in range(10, 1000001):
		cups[i] = {'prev': i - 1, 'next': i + 1}
	cups[10]['prev'] = int(init[-1])
	cups[cups[10]['prev']]['next'] = 10
	cups[1000000]['next'] = int(init[0])
	cups[cups[1000000]['next']]['prev'] = 1000000

	mark = int(init[0])
	for it in range(10000000):
		buff = [cups[mark]['next']]
		buff += [cups[buff[-1]]['next']]
		buff += [cups[buff[-1]]['next']]

		destination = mark
		while destination == mark or destination in buff:
			destination -= 1
			if destination == 0:
				destination = max(list(cups.keys()))

		cups[mark]['next'], cups[cups[buff[-1]]['next']]['prev'], cups[buff[-1]]['next'], cups[cups[destination]['next']]['prev'], cups[destination]['next'], cups[buff[0]]['prev'] = cups[buff[-1]]['next'], mark, cups[destination]['next'], buff[-1], buff[0], destination

		mark = cups[mark]['next']

	print(cups[1]['next']*cups[cups[1]['next']]['next'])


if __name__ == '__main__':
	day_23_task_1()
	day_23_task_2()
