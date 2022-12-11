#include <bits/stdc++.h>
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <sstream>
#include <queue>

#define dump(...)		cerr << "[" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "]" << endl
#define arr_dump(...)		cerr << "[" << #__VA_ARGS__ "(" << sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]) << "): ["; for (unsigned long long int it = 0; it < sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]); ++it) cerr << (__VA_ARGS__)[it] << (it + 1 < sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]) ? ", " : ""); cerr << "]]" << endl
#define vec_dump(...)		cerr << "[" << #__VA_ARGS__ "(" << (__VA_ARGS__).size() << "): ["; for (auto it = (__VA_ARGS__).begin(); it != (__VA_ARGS__).end(); ++it) cerr << *it << (it + 1 != (__VA_ARGS__).end() ? ", " : ""); cerr << "]]" << endl
#define pair_dump(...)		cerr << "[" << #__VA_ARGS__ ": (" << it->first << ", " << it->second << ")]" << endl
#define vec_pair_dump(...)	cerr << "[" << #__VA_ARGS__ "(" << (__VA_ARGS__).size() << "): ["; for (auto it = (__VA_ARGS__).begin(); it != (__VA_ARGS__).end(); ++it) cerr << "(" << it->first << ", " << it->second << ")" << (it + 1 != (__VA_ARGS__).end() ? ", " : ""); cerr << "]]" << endl

using namespace std;

/*
 * --- Day 11: Monkey in the Middle ---
 * --- Part Two ---
 *
 *  You're worried you might not ever get your items back. So worried, in fact,
 *  that your relief that a monkey's inspection didn't damage an item no longer
 *  causes your worry level to be divided by three.
 *
 *  Unfortunately, that relief was all that was keeping your worry levels from
 *  reaching ridiculous levels. You'll need to find another way to keep your
 *  worry levels manageable.
 *
 *  At this rate, you might be putting up with these monkeys for a very long
 *  time - possibly 10000 rounds!
 *
 *  With these new rules, you can still figure out the monkey business after
 *  10000 rounds. Using the same example above:
 *
 *  == After round 1 ==
 *  Monkey 0 inspected items 2 times.
 *  Monkey 1 inspected items 4 times.
 *  Monkey 2 inspected items 3 times.
 *  Monkey 3 inspected items 6 times.
 *
 *  == After round 20 ==
 *  Monkey 0 inspected items 99 times.
 *  Monkey 1 inspected items 97 times.
 *  Monkey 2 inspected items 8 times.
 *  Monkey 3 inspected items 103 times.
 *
 *  == After round 1000 ==
 *  Monkey 0 inspected items 5204 times.
 *  Monkey 1 inspected items 4792 times.
 *  Monkey 2 inspected items 199 times.
 *  Monkey 3 inspected items 5192 times.
 *
 *  == After round 2000 ==
 *  Monkey 0 inspected items 10419 times.
 *  Monkey 1 inspected items 9577 times.
 *  Monkey 2 inspected items 392 times.
 *  Monkey 3 inspected items 10391 times.
 *
 *  == After round 3000 ==
 *  Monkey 0 inspected items 15638 times.
 *  Monkey 1 inspected items 14358 times.
 *  Monkey 2 inspected items 587 times.
 *  Monkey 3 inspected items 15593 times.
 *
 *  == After round 4000 ==
 *  Monkey 0 inspected items 20858 times.
 *  Monkey 1 inspected items 19138 times.
 *  Monkey 2 inspected items 780 times.
 *  Monkey 3 inspected items 20797 times.
 *
 *  == After round 5000 ==
 *  Monkey 0 inspected items 26075 times.
 *  Monkey 1 inspected items 23921 times.
 *  Monkey 2 inspected items 974 times.
 *  Monkey 3 inspected items 26000 times.
 *
 *  == After round 6000 ==
 *  Monkey 0 inspected items 31294 times.
 *  Monkey 1 inspected items 28702 times.
 *  Monkey 2 inspected items 1165 times.
 *  Monkey 3 inspected items 31204 times.
 *
 *  == After round 7000 ==
 *  Monkey 0 inspected items 36508 times.
 *  Monkey 1 inspected items 33488 times.
 *  Monkey 2 inspected items 1360 times.
 *  Monkey 3 inspected items 36400 times.
 *
 *  == After round 8000 ==
 *  Monkey 0 inspected items 41728 times.
 *  Monkey 1 inspected items 38268 times.
 *  Monkey 2 inspected items 1553 times.
 *  Monkey 3 inspected items 41606 times.
 *
 *  == After round 9000 ==
 *  Monkey 0 inspected items 46945 times.
 *  Monkey 1 inspected items 43051 times.
 *  Monkey 2 inspected items 1746 times.
 *  Monkey 3 inspected items 46807 times.
 *
 *  == After round 10000 ==
 *  Monkey 0 inspected items 52166 times.
 *  Monkey 1 inspected items 47830 times.
 *  Monkey 2 inspected items 1938 times.
 *  Monkey 3 inspected items 52013 times.
 *
 *  After 10000 rounds, the two most active monkeys inspected items 52166 and
 *  52013 times. Multiplying these together, the level of monkey business in
 *  this situation is now 2713310158.
 *
 *  Worry levels are no longer divided by three after each item is inspected;
 *  you'll need to find another way to keep your worry levels manageable.
 *  Starting again from the initial state in your puzzle input, what is the
 *  level of monkey business after 10000 rounds?
 */

#define N_MONKEYS 	8
#define N_ROUNDS 	10000

class Monkey
{
	public:
		queue <unsigned long long> items;
		bool multiply;
		unsigned long long n;
		unsigned long long modulo;
		short ifs[2];
		unsigned long long inspected_items = 0;

		Monkey(queue <unsigned long long> items, bool mult,
				unsigned long long n, unsigned long long modulo, short t,
				short f) {
			while(!items.empty()) {
				this->items.push(items.front());
				items.pop();
			}
			this->multiply = mult;
			this->n = n;
			this->modulo = modulo;
			this->ifs[0] = f;
			this->ifs[1] = t;
		}

		short inspection(unsigned long long *x) {
			*x = items.front();
			items.pop();

			++inspected_items;
			if (this->multiply)
				*x = (*x)*(this->n == 0? *x: this->n);
			else
				*x = ((*x) + (this->n == 0? *x: this->n));

			return ifs[!((*x)%modulo)];
		}
};

int main()
{
	string line;
	queue <unsigned long long> items;
	char operation;
	unsigned long long n;
	unsigned long long modulo, collective_modulo = 1;
	short t, f;
	vector <Monkey> monkeys;
	stringstream ss;
	unsigned long long most_inspected = 0, second_most_inspected = 0;

	for (short i = 0; i < N_MONKEYS; ++i) {
		getline(cin, line);

		getline(cin, line);
		ss << line.substr(18);
		while (ss >> line)
			items.push(atoll(line.c_str()));
		ss.clear();

		getline(cin, line);
		operation = line[23];
		n = atoll(line.substr(24).c_str());

		getline(cin, line);
		modulo = atoll(line.substr(20).c_str());
		collective_modulo *= modulo;

		getline(cin, line);
		t = atoi(line.substr(28).c_str());

		getline(cin, line);
		f = atoi(line.substr(29).c_str());

		getline(cin, line);

		monkeys.push_back(Monkey(items, operation == '*', n, modulo, t, f));

		while(!items.empty())
			items.pop();
	}

	for (short round = 0; round < N_ROUNDS; ++round) {
		for (short m = 0; m < N_MONKEYS; ++m) {
			while(!monkeys[m].items.empty()) {
				t = monkeys[m].inspection(&n);
				n %= collective_modulo;
				monkeys[t].items.push(n);
			}
		}
	}

	for (short m = 0; m < N_MONKEYS; ++m) {
		cout << "Monkey " << m << ": " << monkeys[m].inspected_items << endl;

		if (monkeys[m].inspected_items >= most_inspected) {
			second_most_inspected = most_inspected;
			most_inspected = monkeys[m].inspected_items;
		} else if (monkeys[m].inspected_items > second_most_inspected) {
			second_most_inspected = monkeys[m].inspected_items;
		}
	}

	cout << endl << "Monkey business: " << most_inspected*second_most_inspected << endl;

	return 0;
}
