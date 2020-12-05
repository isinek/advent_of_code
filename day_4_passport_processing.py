from re import match

class Passport():
	def __init__(self, pass_dict):
		self.fields = {'byr': None, 'iyr': None, 'eyr': None, 'hgt': None, 'hcl': None, 'ecl': None, 'pid': None, 'cid': None}
		for field in pass_dict:
			self.fields[field] = pass_dict[field]

	def is_byr_valid(self):
		return not match(r"^(19[2-9][0-9]|200[0-2])$", str(self.fields['byr'])) == None

	def is_iyr_valid(self):
		return not match(r"^(201[0-9]|2020)$", str(self.fields['iyr'])) == None

	def is_eyr_valid(self):
		return not match(r"^(202[0-9]|2030)$", str(self.fields['eyr'])) == None

	def is_hgt_valid(self):
		return not match(r"^((1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)$", str(self.fields['hgt'])) == None

	def is_hcl_valid(self):
		return not match(r"^#[0-9a-f]{6}$", str(self.fields['hcl'])) == None

	def is_ecl_valid(self):
		return self.fields['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

	def is_pid_valid(self):
		return not match(r"^[0-9]{9}$", str(self.fields['pid'])) == None

	def is_valid(self):
		return self.is_byr_valid() and self.is_iyr_valid() and self.is_eyr_valid() and self.is_hgt_valid() and self.is_hcl_valid() and self.is_ecl_valid() and self.is_pid_valid()


def first_task():
	passports = [{}]
	with open('day_4_passport_processing.in') as f:
		for line in f.readlines():
			if len(line) <= 1:
				passports += [{}]
			else:
				sections = [x.split(':') for x in line.split()]
				for x in sections:
					passports[-1][x[0]] = x[1]
	valid = sum([1 for p in passports if 'hcl' in p and 'iyr' in p and 'eyr' in p and 'ecl' in p and 'pid' in p and 'byr' in p and 'hgt' in p])
	print(valid)


def second_task():
	passports = []
	tmp_pass = {}
	with open('day_4_passport_processing.in') as f:
		for line in f.readlines():
			if len(line) <= 1:
				passports += [Passport(tmp_pass)]
				print(passports[-1].is_valid(), passports[-1].fields)
				tmp_pass = {}
			else:
				sections = [x.split(':') for x in line.split()]
				for x in sections:
					tmp_pass[x[0]] = x[1].strip()
	passports += [Passport(tmp_pass)]
	print(passports[-1].is_valid(), passports[-1].fields)
	valid = sum([p.is_valid() for p in passports])
	print(valid)


if __name__ == '__main__':
	# first_task()
	second_task()
