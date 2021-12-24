'''
--- Day 24: Arithmetic Logic Unit ---
Magic smoke starts leaking from the submarine's arithmetic logic unit (ALU).
Without the ability to perform basic arithmetic and logic functions, the
submarine can't produce cool patterns with its Christmas lights!

It also can't navigate. Or run the oxygen system.

Don't worry, though - you probably have enough oxygen left to give you enough
time to build a new ALU.

The ALU is a four-dimensional processing unit: it has integer variables w, x, y,
and z. These variables all start with the value 0. The ALU also supports six
instructions:
inp a - Read an input value and write it to variable a.
add a b - Add the value of a to the value of b, then store the result in
          variable a.
mul a b - Multiply the value of a by the value of b, then store the result in
          variable a.
div a b - Divide the value of a by the value of b, truncate the result to an
          integer, then store the result in variable a. (Here, "truncate" means
		  to round the value toward zero.)
mod a b - Divide the value of a by the value of b, then store the remainder in
          variable a. (This is also called the modulo operation.)
eql a b - If the value of a and b are equal, then store the value 1 in variable
          a. Otherwise, store the value 0 in variable a.

In all of these instructions, a and b are placeholders; a will always be the
variable where the result of the operation is stored (one of w, x, y, or z),
while b can be either a variable or a number. Numbers can be positive or
negative, but will always be integers.

The ALU has no jump instructions; in an ALU program, every instruction is run
exactly once in order from top to bottom. The program halts after the last
instruction has finished executing.

(Program authors should be especially cautious; attempting to execute div with
b=0 or attempting to execute mod with a<0 or b<=0 will cause the program to
crash and might even damage the ALU. These operations are never intended in any
serious ALU program.)

For example, here is an ALU program which takes an input number, negates it, and
stores it in x:
inp x
mul x -1

Here is an ALU program which takes two input numbers, then sets z to 1 if the
second input number is three times larger than the first input number, or sets z
to 0 otherwise:
inp z
inp x
mul z 3
eql z x

Here is an ALU program which takes a non-negative integer as input, converts it
into binary, and stores the lowest (1's) bit in z, the second-lowest (2's) bit
in y, the third-lowest (4's) bit in x, and the fourth-lowest (8's) bit in w:
inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2

Once you have built a replacement ALU, you can install it in the submarine,
which will immediately resume what it was doing when the ALU failed: validating
the submarine's model number. To do this, the ALU will run the MOdel Number
Automatic Detector program (MONAD, your puzzle input).

Submarine model numbers are always fourteen-digit numbers consisting only of
digits 1 through 9. The digit 0 cannot appear in a model number.

When MONAD checks a hypothetical fourteen-digit model number, it uses fourteen
separate inp instructions, each expecting a single digit of the model number in
order of most to least significant. (So, to check the model number
13579246899999, you would give 1 to the first inp instruction, 3 to the second
inp instruction, 5 to the third inp instruction, and so on.) This means that
when operating MONAD, each input instruction should only ever be given an
integer value of at least 1 and at most 9.

Then, after MONAD has finished running all of its instructions, it will indicate
that the model number was valid by leaving a 0 in variable z. However, if the
model number was invalid, it will leave some other non-zero value in z.

MONAD imposes additional, mysterious restrictions on model numbers, and legend
says the last copy of the MONAD documentation was eaten by a tanuki. You'll need
to figure out what MONAD does some other way.

To enable as many submarine features as possible, find the largest valid
fourteen-digit model number that contains no 0 digits. What is the largest model
number accepted by MONAD?
'''
def find_max(orig_model_number, instructions, orig_var):
	instruction_set = instructions.pop(0)
	smaller_result = False
	for i in range(9, 0, -1):
		model_number = orig_model_number + str(i)
		var = orig_var.copy()
		for args in instruction_set:
			n = -999999
			reg = args[1]
			if len(args) > 2:
				try:
					n = int(args[2])
					if args[1] == 'x' and n < 0:
						smaller_result = True
				except:
					n = var[args[2]]

			if args[0] == 'inp':
				var[reg] = i
			elif args[0] == 'add':
				var[reg] += n
			elif args[0] == 'mul':
				var[reg] *= n
			elif args[0] == 'div':
				var[reg] = var[reg]//n
			elif args[0] == 'mod':
				var[reg] %= n
			elif args[0] == 'eql':
				var[reg] = int(var[reg] == n)

		if len(model_number) == 14 and var['z'] == 0:
			return model_number, var
		if len(instructions) and ((not smaller_result and orig_var['z'] < var['z']) or (smaller_result and orig_var['z']//2 > var['z'])):
			new_model_number, new_var = find_max(model_number, instructions[:], var)
			if len(new_model_number) == 14 and new_var['z'] == 0:
				return new_model_number, new_var

	return '', {}


def day_24_task_1():
	instructions = []
	with open('day_24_arithmetic_logic_unit.in') as f:
		for line in f.readlines():
			args = line.split()
			if args[0] == 'inp':
				instructions += [[]]
			instructions[-1] += [line.split()]

	model, var = find_max('', instructions, {'w': 0, 'x': 0, 'y': 0, 'z': 0})
	print(model)


'''
--- Part Two ---
As the submarine starts booting up things like the Retro Encabulator, you
realize that maybe you don't need all these submarine features after all.

What is the smallest model number accepted by MONAD?
'''
def find_min(orig_model_number, instructions, orig_var):
	instruction_set = instructions.pop(0)
	smaller_result = False
	for i in range(1, 10):
		model_number = orig_model_number + str(i)
		var = orig_var.copy()
		for args in instruction_set:
			n = -999999
			reg = args[1]
			if len(args) > 2:
				try:
					n = int(args[2])
					if args[1] == 'x' and n < 0:
						smaller_result = True
				except:
					n = var[args[2]]

			if args[0] == 'inp':
				var[reg] = i
			elif args[0] == 'add':
				var[reg] += n
			elif args[0] == 'mul':
				var[reg] *= n
			elif args[0] == 'div':
				var[reg] = var[reg]//n
			elif args[0] == 'mod':
				var[reg] %= n
			elif args[0] == 'eql':
				var[reg] = int(var[reg] == n)

		if len(model_number) == 14 and var['z'] == 0:
			return model_number, var
		if len(instructions) and ((not smaller_result and orig_var['z'] < var['z']) or (smaller_result and orig_var['z']//2 > var['z'])):
			new_model_number, new_var = find_min(model_number, instructions[:], var)
			if len(new_model_number) == 14 and new_var['z'] == 0:
				return new_model_number, new_var

	return '', {}


def day_24_task_2():
	instructions = []
	with open('day_24_arithmetic_logic_unit.in') as f:
		for line in f.readlines():
			args = line.split()
			if args[0] == 'inp':
				instructions += [[]]
			instructions[-1] += [line.split()]

	model, var = find_min('', instructions, {'w': 0, 'x': 0, 'y': 0, 'z': 0})
	print(model)


if __name__ == '__main__':
	day_24_task_1()
	day_24_task_2()
