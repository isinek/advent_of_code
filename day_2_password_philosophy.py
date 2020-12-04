def first_task():
	n = int(input())
	valid_passwords = 0
	for i in range(n):
		line = input().split()
		a, b = [int(x) for x in line[0].split('-')]
		c = line[1][0]
		password = line[2]
		count = len([x for x in password if x == c])
		if a <= count <= b:
			valid_passwords += 1
	print(valid_passwords)


def second_task():
	n = int(input())
	valid_passwords = 0
	for i in range(n):
		line = input().split()
		a, b = [int(x) for x in line[0].split('-')]
		c = line[1][0]
		password = line[2]
		res = (password[a - 1] == c) + (password[b - 1] == c)
		if res == 1:
			valid_passwords += 1
	print(valid_passwords)


if __name__ == '__main__':
	# first_task()
	second_task()
