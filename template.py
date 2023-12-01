'''

'''
def day_1_task_1():
	nums = []
	with open('day_1.in') as f:
		for line in f.readlines():
			nums += [int(line)]
		print(nums[-1])


'''

'''
def day_1_task_2():
	nums = []
	with open('day_1.in') as f:
		for line in f.readlines():
			nums += [int(line)]
		print(sum(nums))


if __name__ == '__main__':
	day_1_task_1()
	day_1_task_2()
