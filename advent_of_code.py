from sys import argv

from day_1_sonar_sweep import day_1_task_1, day_1_task_2
from day_2_dive import day_2_task_1, day_2_task_2
from day_3_binary_diagnostic import day_3_task_1, day_3_task_2
from day_4_giant_squid import day_4_task_1, day_4_task_2
from day_5_hydrothermal_venture import day_5_task_1, day_5_task_2
from day_6_lanternfish import day_6_task_1, day_6_task_2
from day_7_the_treachery_of_whales import day_7_task_1, day_7_task_2
from day_8_seven_segment_search import day_8_task_1, day_8_task_2
from day_9_smoke_basin import day_9_task_1, day_9_task_2
from day_10_syntax_scoring import day_10_task_1, day_10_task_2
from day_11_dumbo_octopus import day_11_task_1, day_11_task_2


def print_help():
	print('advent_of_code.py [-d day] [-t task]')
	print('    -d day  - day has values 1-25')
	print('    -t task - task has values 1 or 2')
	print('For other info check: https://adventofcode.com/')


if __name__ == '__main__':
	if '-d' in argv:
		arg_i = argv.index('-d')
		if arg_i + 1 > len(argv) - 1 or int(argv[arg_i + 1]) < 1 or int(argv[arg_i + 1]) > 25:
			print_help()
			exit(1)

		days = [int(argv[arg_i + 1])]
	else:
		days = [i for i in range(1, 26)]

	if '-t' in argv:
		arg_i = argv.index('-t')
		if arg_i + 1 > len(argv) - 1 or not int(argv[arg_i + 1]) in [1, 2]:
			print_help()
			exit(2)

		tasks = [int(argv[arg_i + 1])]
	else:
		tasks = [1, 2]

	for d in days:
		for t in tasks:
			try:
				print('Day', d, 'task', t, '- ', end='')
				locals()[f'day_{d}_task_{t}']()
			except:
				print('Solution does not exist!')
				exit(3)
