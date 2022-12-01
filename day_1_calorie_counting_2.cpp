#include <bits/stdc++.h>
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>

#define dump(...)		cerr << "[" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "]" << endl
#define arr_dump(...)		cerr << "[" << #__VA_ARGS__ "(" << sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]) << "): ["; for (unsigned long long int it = 0; it < sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]); ++it) cerr << (__VA_ARGS__)[it] << (it + 1 < sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]) ? ", " : ""); cerr << "]]" << endl
#define vec_dump(...)		cerr << "[" << #__VA_ARGS__ "(" << (__VA_ARGS__).size() << "): ["; for (auto it = (__VA_ARGS__).begin(); it != (__VA_ARGS__).end(); ++it) cerr << *it << (it + 1 != (__VA_ARGS__).end() ? ", " : ""); cerr << "]]" << endl
#define pair_dump(...)		cerr << "[" << #__VA_ARGS__ ": (" << it->first << ", " << it->second << ")]" << endl
#define vec_pair_dump(...)	cerr << "[" << #__VA_ARGS__ "(" << (__VA_ARGS__).size() << "): ["; for (auto it = (__VA_ARGS__).begin(); it != (__VA_ARGS__).end(); ++it) cerr << "(" << it->first << ", " << it->second << ")" << (it + 1 != (__VA_ARGS__).end() ? ", " : ""); cerr << "]]" << endl

using namespace std;

/*
 * --- Day 1: Calorie Counting ---
 *  --- Part Two ---
 *  By the time you calculate the answer to the Elves' question, they've already
 *  realized that the Elf carrying the most Calories of food might eventually
 *  run out of snacks.
 *
 *  To avoid this unacceptable situation, the Elves would instead like to know
 *  the total Calories carried by the top three Elves carrying the most
 *  Calories. That way, even if one of those Elves runs out of snacks, they
 *  still have two backups.
 *
 *  In the example above, the top three Elves are the fourth Elf (with 24000
 *  Calories), then the third Elf (with 11000 Calories), then the fifth Elf
 *  (with 10000 Calories). The sum of the Calories carried by these three elves
 *  is 45000.
 *
 *  Find the top three Elves carrying the most Calories. How many Calories are
 *  those Elves carrying in total?
*/

int main()
{
	string line;
	vector <unsigned int> cals;
	unsigned int i = 0;

	cals.push_back(0);
	while (true) {
		getline(cin, line);
		if (!line.length()) {
			if (!cals[i])
				break;

			cals.push_back(0);
			++i;
		} else {
			cals[i] += stoi(line);
		}
	}

	sort(cals.begin(), cals.end(), greater<unsigned int>());

	cout << cals[0] + cals[1] + cals[2] << endl;

	return 0;
}
