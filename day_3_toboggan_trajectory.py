def first_task():
	n = int(input())
	pattern = [input() for _ in range(n)]
	position = {'x': 0, 'y': 0}
	trees = 0
	for _ in range(n - 1):
		position['x'] = (position['x'] + 3) % len(pattern[0])
		position['y'] += 1
		if pattern[position['y']][position['x']] == '#':
			trees += 1
	print(trees)


def second_task():
	n = int(input())
	pattern = [input() for _ in range(n)]
	slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
	trees = [0]*len(slopes)
	for i in range(1, n):
		for j in range(len(slopes)):
			if slopes[j][1]*i > n - 1:
				continue
			if pattern[slopes[j][1]*i][(slopes[j][0]*i) % len(pattern[0])] == '#':
				trees[j] += 1
	res = 1
	for x in trees:
		res *= x
	print(res)


if __name__ == '__main__':
	# first_task()
	second_task()
