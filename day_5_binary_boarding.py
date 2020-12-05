def first_task():
	max_seat = 0
	with open('day_5_binary_boarding.in') as f:
		for line in f.readlines():
			seat = {'r': {'l': 0, 'u': 127}, 'c': {'l': 0, 'u': 7}}
			for c in line[:7]:
				if c == 'B':
					seat['r']['l'] = (seat['r']['l'] + seat['r']['u'] + 1) // 2
				else:
					seat['r']['u'] = (seat['r']['l'] + seat['r']['u']) // 2
			for c in line[7:]:
				if c == 'R':
					seat['c']['l'] = (seat['c']['l'] + seat['c']['u'] + 1) // 2
				else:
					seat['c']['u'] = (seat['c']['l'] + seat['c']['u']) // 2
			seat_id = seat['r']['l'] * 8 + seat['c']['l']
			if seat_id > max_seat:
				max_seat = seat_id
	print(max_seat)


def second_task():
	plane_map = [0 for _ in range(1024)]
	with open('day_5_binary_boarding.in') as f:
		for line in f.readlines():
			seat = {'r': {'l': 0, 'u': 127}, 'c': {'l': 0, 'u': 7}}
			for c in line[:7]:
				if c == 'B':
					seat['r']['l'] = (seat['r']['l'] + seat['r']['u'] + 1) // 2
				else:
					seat['r']['u'] = (seat['r']['l'] + seat['r']['u']) // 2
			for c in line[7:]:
				if c == 'R':
					seat['c']['l'] = (seat['c']['l'] + seat['c']['u'] + 1) // 2
				else:
					seat['c']['u'] = (seat['c']['l'] + seat['c']['u']) // 2
			seat_id = seat['r']['l']*8 + seat['c']['l']
			plane_map[seat_id] = 1
	for i in range(1, 127):
		for j in range(8):
			if plane_map[i*8 + j] == 0 and plane_map[i*8 + j + 1] == plane_map[i*8 + j - 1] and plane_map[i*8 + j - 1] == 1:
				print(i*8 + j)


if __name__ == '__main__':
	# first_task()
	second_task()
