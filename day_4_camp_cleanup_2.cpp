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
 * --- Day 4: Camp Cleanup ---
 * --- Part Two ---
 *
 *  It seems like there is still quite a bit of duplicate work planned. Instead,
 *  the Elves would like to know the number of pairs that overlap at all.
 *  In the above example, the first two pairs (2-4,6-8 and 2-3,4-5) don't
 *  overlap, while the remaining four pairs (5-7,7-9, 2-8,3-7, 6-6,4-6, and
 *  2-6,4-8) do overlap:
 *
 *  - 5-7,7-9 overlaps in a single section, 7.
 *  - 2-8,3-7 overlaps all of the sections 3 through 7.
 *  - 6-6,4-6 overlaps in a single section, 6.
 *  - 2-6,4-8 overlaps in sections 4, 5, and 6.
 *
 *  So, in this example, the number of overlapping assignment pairs is 4.
 *
 *  In how many assignment pairs do the ranges overlap?
 */

#define N_INPUTS 1000

int main()
{
	unsigned int r[2][2];
	unsigned int overlaping_ranges = 0;

	for (short i = 0; i < N_INPUTS; ++i) {
		scanf("%u-%u,%u-%u", &r[0][0], &r[0][1], &r[1][0], &r[1][1]);

		if ((r[0][0] <= r[1][0] && r[0][1] >= r[1][0]) ||
				(r[0][0] <= r[1][1] && r[0][1] >= r[1][1]) ||
				(r[1][0] <= r[0][0] && r[1][1] >= r[0][0]) ||
				(r[1][0] <= r[0][1] && r[1][1] >= r[0][1]))
			++overlaping_ranges;
	}

	cout << overlaping_ranges << endl;

	return 0;
}
