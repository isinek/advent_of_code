def first_task():
	looping = True
	nums = []
	while looping:
		nn = int(input())
		if nn:
			for n in nums:
				if nn + n == 2020:
					print(nn * n)
					looping = False
					break
			nums += [nn]
		else:
			break


def second_task():
	looping = True
	nums = []
	pairs = []
	while looping:
		nn = int(input())
		if nn:
			for p in pairs:
				if p['sum'] + nn == 2020:
					print(p['product']*nn)
					looping = False
					break
			if looping:
				for n in nums:
					if nn + n < 2020:
						pairs += [{'sum': nn + n, 'product': nn*n}]
			nums += [nn]
		else:
			break


if __name__ == '__main__':
	# first_task()
	second_task()
