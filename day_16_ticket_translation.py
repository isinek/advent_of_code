'''
--- Day 16: Ticket Translation ---
As you're walking to yet another connecting flight, you realize that one of the
legs of your re-routed trip coming up is on a high-speed train. However, the
train ticket you were given is in a language you don't understand. You should
probably figure out what it says before you get to the train station after the
next flight.

Unfortunately, you can't actually read the words on the ticket. You can,
however, read the numbers, and so you figure out the fields these tickets must
have and the valid ranges for values in those fields.

You collect the rules for ticket fields, the numbers on your ticket, and the
numbers on other nearby tickets for the same train service (via the airport
security cameras) together into a single document you can reference (your puzzle
input).

The rules for ticket fields specify a list of fields that exist somewhere on the
ticket and the valid ranges of values for each field. For example, a rule like
class: 1-3 or 5-7 means that one of the fields in every ticket is named class
and can be any value in the ranges 1-3 or 5-7 (inclusive, such that 3 and 5 are
both valid in this field, but 4 is not).

Each ticket is represented by a single line of comma-separated values. The
values are the numbers on the ticket in the order they appear; every ticket has
the same format. For example, consider this ticket:

.--------------------------------------------------------.
| ????: 101    ?????: 102   ??????????: 103     ???: 104 |
|                                                        |
| ??: 301  ??: 302             ???????: 303      ??????? |
| ??: 401  ??: 402           ???? ????: 403    ????????? |
'--------------------------------------------------------'
Here, ? represents text in a language you don't understand. This ticket might be
represented as 101,102,103,104,301,302,303,401,402,403; of course, the actual
train tickets you're looking at are much more complicated. In any case, you've
extracted just the numbers in such a way that the first number is always the
same specific field, the second number is always a different specific field, and
so on - you just don't know what each position actually means!

Start by determining which tickets are completely invalid; these are tickets
that contain values which aren't valid for any field. Ignore your ticket for
now.

For example, suppose you have the following notes:

class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12
It doesn't matter which position corresponds to which field; you can identify
invalid nearby tickets by considering only whether tickets contain values that
are not valid for any field. In this example, the values on the first nearby
ticket are all valid for at least one field. This is not true of the other three
nearby tickets: the values 4, 55, and 12 are are not valid for any field. Adding
together all of the invalid values produces your ticket scanning error
rate: 4 + 55 + 12 = 71.

Consider the validity of the nearby tickets you scanned. What is your ticket
scanning error rate?
'''
def day_16_task_1():
	with open('day_16_ticket_translation.in') as f:
		rules = []
		while True:
			tmp = f.readline().strip('\n').split()
			if not len(tmp):
				break
			rules += [[int(y) for y in x.split('-')] for x in tmp if '-' in x]
		valid_nums = []
		for r in rules:
			for i in range(r[0], r[1] + 1):
				if not i in valid_nums:
					valid_nums += [i]

		# my ticket
		f.readline()
		f.readline()
		f.readline()

		# nearby tickets
		f.readline()
		invalid_sum = 0
		for line in f.readlines():
			for x in line.split(','):
				n = int(x)
				if not n in valid_nums:
					invalid_sum += n
		print(invalid_sum)


'''
--- Part Two ---
Now that you've identified which tickets contain invalid values, discard those
tickets entirely. Use the remaining valid tickets to determine which field is
which.

Using the valid ranges for each field, determine what order the fields appear on
the tickets. The order is consistent between all tickets: if seat is the third
field, it is the third field on every ticket, including your ticket.

For example, suppose you have the following notes:

class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9
Based on the nearby tickets in the above example, the first position must be
row, the second position must be class, and the third position must be seat; you
can conclude that in your ticket, class is 12, row is 11, and seat is 13.

Once you work out which field is which, look for the six fields on your ticket
that start with the word departure. What do you get if you multiply those six
values together?
'''
def day_16_task_2():
	with open('day_16_ticket_translation.in') as f:
		valid_nums = {}
		all_valid_nums = []
		while True:
			tmp = f.readline().strip('\n').split(': ')
			if len(tmp) < 2:
				break
			field = tmp[0]
			tmp = tmp[1].strip().split()
			rules = [[int(y) for y in x.split('-')] for x in tmp if '-' in x]
			valid_nums[field] = []
			for r in rules:
				valid_nums[field] += range(r[0], r[1] + 1)
				all_valid_nums += valid_nums[field]

		field_map = {}
		for x in valid_nums:
			field_map[x] = [*range(0, len(valid_nums))]

		# my ticket
		f.readline()
		my_ticket = [int(x) for x in f.readline().strip('\n').split(',')]

		# nearby tickets
		f.readline()
		f.readline()
		for line in f.readlines():
			ticket = [int(x) for x in line.strip('\n').split(',')]
			if not all([n in all_valid_nums for n in ticket]):
				continue
			for i, n in enumerate(ticket):
				for field in valid_nums:
					if not i in field_map[field]:
						continue
					elif not n in valid_nums[field]:
						field_map[field].remove(i)

		while not all([len(field_map[field]) == 1 for field in field_map]):
			for f1 in field_map:
				for i in field_map[f1][:]:
					unique = True
					for f2 in field_map:
						if f1 == f2:
							continue
						elif i in field_map[f2]:
							unique = False
							break
					if unique:
						field_map[f1] = [i]

			for f1 in field_map:
				if len(field_map[f1]) == 1:
					i = field_map[f1][0]
					for f2 in field_map:
						if i in field_map[f2] and f1 != f2:
							field_map[f2].remove(i)

		res = 1
		for x in field_map:
			if 'departure' in x:
				res *= my_ticket[field_map[x][0]]
		print(res)


if __name__ == '__main__':
	day_16_task_1()
	day_16_task_2()
