from sys import argv

from day_1_report_repair import day_1_task_1, day_1_task_2
from day_2_password_philosophy import day_2_task_1, day_2_task_2
from day_3_toboggan_trajectory import day_3_task_1, day_3_task_2
from day_4_passport_processing import day_4_task_1, day_4_task_2
from day_5_binary_boarding import day_5_task_1, day_5_task_2
from day_6_custom_customs import day_6_task_1, day_6_task_2
from day_7_handy_haversacks import day_7_task_1, day_7_task_2
from day_8_handheld_halting import day_8_task_1, day_8_task_2
from day_9_encoding_error import day_9_task_1, day_9_task_2
from day_10_adapter_array import day_10_task_1, day_10_task_2
from day_11_seating_system import day_11_task_1, day_11_task_2
from day_12_rain_risk import day_12_task_1, day_12_task_2


def print_help():
	print('advent_of_code_2020.py [-d day] [-t task]')
	print('    -d day  - day has values 1-25')
	print('    -t task - task has values 1 or 2')
	print('For other info check: https://adventofcode.com/2020/')


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
			exit(1)

		tasks = [int(argv[arg_i + 1])]
	else:
		tasks = [1, 2]

	for d in days:
		for t in tasks:
			try:
				print('Day', d, 'task', t, '- ', end='')
				locals()['day_{}_task_{}'.format(d, t)]()
			except:
				print('Solution does not exist yet!')
				exit(0)
