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
 * --- Day 3: Rucksack Reorganization ---
 *  --- Part Two ---
 *
 *  As you finish identifying the misplaced items, the Elves come to you with
 *  another issue.
 *
 *  For safety, the Elves are divided into groups of three. Every Elf carries a
 *  badge that identifies their group. For efficiency, within each group of
 *  three Elves, the badge is the only item type carried by all three Elves.
 *  That is, if a group's badge is item type B, then all three Elves will have
 *  item type B somewhere in their rucksack, and at most two of the Elves will
 *  be carrying any other item type.
 *
 *  The problem is that someone forgot to put this year's updated authenticity
 *  sticker on the badges. All of the badges need to be pulled out of the
 *  rucksacks so the new authenticity stickers can be attached.
 *
 * Additionally, nobody wrote down which item type corresponds to each group's
 * badges. The only way to tell which item type is the right one is by finding
 * the one item type that is common between all three Elves in each group.
 *
 * Every set of three lines in your list corresponds to a single group, but each
 * group can have a different badge item type. So, in the above example, the
 * first group's rucksacks are the first three lines:
 *
 * vJrwpWtwJgWrhcsFMMfFFhFp
 * jqHRNqRjqzjGDLGLrsFMfFZSrLrFZsSL
 * PmmdzqPrVvPwwTWBwg
 *
 * And the second group's rucksacks are the next three lines:
 *
 * wMqvLMZHhHMvwLHjbvcjnnSBnvTQFn
 * ttgJtRGJQctTZtZT
 * CrZsJsPPZsGzwwsLwLmpwMDw
 *
 * In the first group, the only item type that appears in all three rucksacks is
 * lowercase r; this must be their badges. In the second group, their badge item
 * type must be Z.
 *
 * Priorities for these items must still be found to organize the sticker
 * attachment efforts: here, they are 18 (r) for the first group and 52 (Z) for
 * the second group. The sum of these is 70.
 *
 * Find the item type that corresponds to the badges of each three-Elf group.
 * What is the sum of the priorities of those item types?
 */

#define N_INPUTS 300

int main()
{
	string rucksack_group[3];
	unsigned long prio_sum = 0;
	bool badge;
	char c;

	for (short i = 0; i < N_INPUTS/3; ++i) {
		for (short j = 0; j < 3; ++j)
			cin >> rucksack_group[j];

		badge = false;
		c = 'a';
		while (!badge) {
			badge = true;
			for (short k = 0; k < 3; ++k) {
				if (rucksack_group[k].find(c) == string::npos) {
					badge = false;
					break;
				}
			}
			if (badge && c >= 'a') {
				prio_sum += c - 'a' + 1;
				break;
			} else if (badge) {
				prio_sum += c - 'A' + 27;
				break;
			}

			if (c != 'z')
				++c;
			else
				c = 'A';
		}
	}

	cout << prio_sum << endl;

	return 0;
}
