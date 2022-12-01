#include <bits/stdc++.h>
#include <iostream>
#include <cstdlib>
#include <string>

#define dump(...)		cerr << "[" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "]" << endl
#define arr_dump(...)		cerr << "[" << #__VA_ARGS__ "(" << sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]) << "): ["; for (unsigned long long int it = 0; it < sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]); ++it) cerr << (__VA_ARGS__)[it] << (it + 1 < sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]) ? ", " : ""); cerr << "]]" << endl
#define vec_dump(...)		cerr << "[" << #__VA_ARGS__ "(" << (__VA_ARGS__).size() << "): ["; for (auto it = (__VA_ARGS__).begin(); it != (__VA_ARGS__).end(); ++it) cerr << *it << (it + 1 != (__VA_ARGS__).end() ? ", " : ""); cerr << "]]" << endl
#define pair_dump(...)		cerr << "[" << #__VA_ARGS__ ": (" << it->first << ", " << it->second << ")]" << endl
#define vec_pair_dump(...)	cerr << "[" << #__VA_ARGS__ "(" << (__VA_ARGS__).size() << "): ["; for (auto it = (__VA_ARGS__).begin(); it != (__VA_ARGS__).end(); ++it) cerr << "(" << it->first << ", " << it->second << ")" << (it + 1 != (__VA_ARGS__).end() ? ", " : ""); cerr << "]]" << endl

using namespace std;

/*
 * --- Day 1: Calorie Counting ---
 *  The jungle must be too overgrown and difficult to navigate in vehicles or
 *  access from the air; the Elves' expedition traditionally goes on foot. As
 *  your boats approach land, the Elves begin taking inventory of their
 *  supplies. One important consideration is food - in particular, the number
 *  of Calories each Elf is carrying (your puzzle input).
 *
 *  The Elves take turns writing down the number of Calories contained by the
 *  various meals, snacks, rations, etc. that they've brought with them, one
 *  item per line. Each Elf separates their own inventory from the previous
 *  Elf's inventory (if any) by a blank line.
 *
 *  For example, suppose the Elves finish writing their items' Calories and end
 *  up with the following list:
 *
 *  1000
 *  2000
 *  3000
 *
 *  4000
 *
 *  5000
 *  6000
 *
 *  7000
 *  8000
 *  9000
 *
 *  10000
 *  This list represents the Calories of the food carried by five Elves:
 *
 *  The first Elf is carrying food with 1000, 2000, and 3000 Calories, a total
 *  of 6000 Calories.
 *  The second Elf is carrying one food item with 4000 Calories.
 *  The third Elf is carrying food with 5000 and 6000 Calories, a total of
 *  11000 Calories.
 *  The fourth Elf is carrying food with 7000, 8000, and 9000 Calories, a total
 *  of 24000 Calories.
 *  The fifth Elf is carrying one food item with 10000 Calories.
 *  In case the Elves get hungry and need extra snacks, they need to know which
 *  Elf to ask: they'd like to know how many Calories are being carried by the
 *  Elf carrying the most Calories. In the example above, this is 24000 (carried
 *  by the fourth Elf).
 *
 *  Find the Elf carrying the most Calories. How many total Calories is that Elf
 *  carrying?
*/

int main()
{
	string line;
	unsigned int max_cals = 0, cals = 0;

	while (true) {
		getline(cin, line);
		if (!line.length()) {
			if (!cals)
				break;

			if (cals > max_cals)
				max_cals = cals;
			cals = 0;
		} else {
			cals += stoi(line);
		}
	}
	cout << max_cals << endl;

	return 0;
}
