'''
--- Day 14: Extended Polymerization ---
The incredible pressures at this depth are starting to put a strain on your
submarine. The submarine has polymerization equipment that would produce
suitable materials to reinforce the submarine, and the nearby
volcanically-active caves should even have the necessary input elements in
sufficient quantities.

The submarine manual contains instructions for finding the optimal polymer
formula; specifically, it offers a polymer template and a list of pair insertion
rules (your puzzle input). You just need to work out what polymer would result
after repeating the pair insertion process a few times.

For example:
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C

The first line is the polymer template - this is the starting point of the
process.

The following section defines the pair insertion rules. A rule like AB -> C
means that when elements A and B are immediately adjacent, element C should be
inserted between them. These insertions all happen simultaneously.

So, starting with the polymer template NNCB, the first step simultaneously
considers all three pairs:
 - The first pair (NN) matches the rule NN -> C, so element C is inserted
   between the first N and the second N.
 - The second pair (NC) matches the rule NC -> B, so element B is inserted
   between the N and the C.
 - The third pair (CB) matches the rule CB -> H, so element H is inserted
   between the C and the B.

Note that these pairs overlap: the second element of one pair is the first
element of the next pair. Also, because all pairs are considered simultaneously,
inserted elements are not considered to be part of a pair until the next step.

After the first step of this process, the polymer becomes NCNBCHB.

Here are the results of a few steps using the above rules:
Template:     NNCB
After step 1: NCNBCHB
After step 2: NBCCNBBBCBHCB
After step 3: NBBBCNCCNBBNBNBBCHBHHBCHB
After step 4: NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB

This polymer grows quickly. After step 5, it has length 97; After step 10, it
has length 3073. After step 10, B occurs 1749 times, C occurs 298 times, H
occurs 161 times, and N occurs 865 times; taking the quantity of the most common
element (B, 1749) and subtracting the quantity of the least common element
(H, 161) produces 1749 - 161 = 1588.

Apply 10 steps of pair insertion to the polymer template and find the most and
least common elements in the result. What do you get if you take the quantity of
the most common element and subtract the quantity of the least common element?
'''
def day_14_task_1():
	polymer = ''
	pairs = {}
	with open('day_14_extended_polymerization.in') as f:
		polymer = f.readline().replace('\n', '')
		f.readline()
		for line in f.readlines():
			p, ins = line.replace('\n', '').split(' -> ')
			pairs[p] = ins

	elements = {}
	for e in polymer:
		if e in elements:
			elements[e] += 1
		else:
			elements[e] = 1

	steps = 10
	for _ in range(steps):
		new_polymer = ''
		for i in range(len(polymer) - 1):
			if polymer[i:i + 2] in pairs:
				new_polymer += polymer[i] + pairs[polymer[i:i + 2]]
				if new_polymer[-1] in elements:
					elements[new_polymer[-1]] += 1
				else:
					elements[new_polymer[-1]] = 1
			else:
				new_polymer += polymer[i]
		new_polymer += polymer[-1]
		polymer = new_polymer

	vals = sorted([elements[e] for e in elements])
	print(vals[-1] - vals[0])


'''
--- Part Two ---
The resulting polymer isn't nearly strong enough to reinforce the submarine.
You'll need to run more steps of the pair insertion process; a total of 40 steps
should do it.

In the above example, the most common element is B (occurring 2192039569602
times) and the least common element is H (occurring 3849876073 times);
subtracting these produces 2188189693529.

Apply 40 steps of pair insertion to the polymer template and find the most and
least common elements in the result. What do you get if you take the quantity of
the most common element and subtract the quantity of the least common element?
'''
pairs = {}
memo = {}

def new_elements(pair, steps):
	if not pair in memo:
		return {}
	if steps in memo[pair]:
		return memo[pair][steps]

	memo[pair][steps] = {pairs[pair]: 1}
	elems = new_elements(pair[0] + pairs[pair], steps - 1)
	for e in elems:
		if e in memo[pair][steps]:
			memo[pair][steps][e] += elems[e]
		else:
			memo[pair][steps][e] = elems[e]

	elems = new_elements(pairs[pair] + pair[1], steps - 1)
	for e in elems:
		if e in memo[pair][steps]:
			memo[pair][steps][e] += elems[e]
		else:
			memo[pair][steps][e] = elems[e]

	return memo[pair][steps]


def day_14_task_2():
	polymer = ''
	with open('day_14_extended_polymerization.in') as f:
		polymer = f.readline().replace('\n', '')
		f.readline()
		for line in f.readlines():
			p, ins = line.replace('\n', '').split(' -> ')
			pairs[p] = ins
			memo[p] = {1: {ins: 1}}

	elements = {}
	steps = 40
	q = []
	for i in range(len(polymer) - 1):
		if polymer[i] in elements:
			elements[polymer[i]] += 1
		else:
			elements[polymer[i]] = 1
		new_elems = new_elements(polymer[i:i + 2], steps)
		for e in new_elems:
			if e in elements:
				elements[e] += new_elems[e]
			else:
				elements[e] = new_elems[e]
	if polymer[-1] in elements:
		elements[polymer[-1]] += 1
	else:
		elements[polymer[-1]] = 1

	vals = sorted([elements[e] for e in elements])
	print(vals[-1] - vals[0])


if __name__ == '__main__':
	day_14_task_1()
	day_14_task_2()
