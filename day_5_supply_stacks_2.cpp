#include <iostream>
#include <bits/stdc++.h>
#include <cstdlib>
#include <string>
#include <vector>
#include <algorithm>
#include <stack>
#include <queue>

#define dump(...)		cerr << "[" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "]" << endl
#define arr_dump(...)		cerr << "[" << #__VA_ARGS__ "(" << sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]) << "): ["; for (unsigned long long int it = 0; it < sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]); ++it) cerr << (__VA_ARGS__)[it] << (it + 1 < sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]) ? ", " : ""); cerr << "]]" << endl
#define vec_dump(...)		cerr << "[" << #__VA_ARGS__ "(" << (__VA_ARGS__).size() << "): ["; for (auto it = (__VA_ARGS__).begin(); it != (__VA_ARGS__).end(); ++it) cerr << *it << (it + 1 != (__VA_ARGS__).end() ? ", " : ""); cerr << "]]" << endl
#define pair_dump(...)		cerr << "[" << #__VA_ARGS__ ": (" << it->first << ", " << it->second << ")]" << endl
#define vec_pair_dump(...)	cerr << "[" << #__VA_ARGS__ "(" << (__VA_ARGS__).size() << "): ["; for (auto it = (__VA_ARGS__).begin(); it != (__VA_ARGS__).end(); ++it) cerr << "(" << it->first << ", " << it->second << ")" << (it + 1 != (__VA_ARGS__).end() ? ", " : ""); cerr << "]]" << endl

using namespace std;

/*
 * --- Day 5: Supply Stacks ---
 *  --- Part Two ---
 *  As you watch the crane operator expertly rearrange the crates, you notice
 *  the process isn't following your prediction.
 *
 *  Some mud was covering the writing on the side of the crane, and you quickly
 *  wipe it away. The crane isn't a CrateMover 9000 - it's a CrateMover 9001.
 *
 *  The CrateMover 9001 is notable for many new and exciting features: air
 *  conditioning, leather seats, an extra cup holder, and the ability to pick up
 *  and move multiple crates at once.
 *
 *  Again considering the example above, the crates begin in the same
 *  configuration:
 *       [D]
 *   [N] [C]
 *   [Z] [M] [P]
 *    1   2   3
 *
 *  Moving a single crate from stack 2 to stack 1 behaves the same as before:
 *   [D]
 *   [N] [C]
 *   [Z] [M] [P]
 *    1   2   3
 *
 *  However, the action of moving three crates from stack 1 to stack 3 means that
 *  those three moved crates stay in the same order, resulting in this new
 *  configuration:
 *           [D]
 *           [N]
 *       [C] [Z]
 *       [M] [P]
 *    1   2   3
 *
 *  Next, as both crates are moved from stack 2 to stack 1, they retain their
 *  order as well:
 *           [D]
 *           [N]
 *   [C]     [Z]
 *   [M]     [P]
 *    1   2   3
 *
 *  Finally, a single crate is still moved from stack 1 to stack 2, but now it's
 *  crate C that gets moved:
 *           [D]
 *           [N]
 *           [Z]
 *   [M] [C] [P]
 *    1   2   3
 *
 *  In this example, the CrateMover 9001 has put the crates in a totally
 *  different order: MCD.
 *
 *  Before the rearrangement process finishes, update your simulation so that
 *  the Elves know where they should stand to be ready to unload the final
 *  supplies. After the rearrangement procedure completes, what crate ends up on
 *  top of each stack?
 */

#define N_STACKS 		9
#define N_MOVES 		501
#define MAX_STACK_SIZE 	60

int main()
{
	stack<char> stacks[N_STACKS];
	stack<char> tmp;
	string line;
	queue<char> invertor;
	unsigned int n, a, b;

	while(true) {
		getline(cin, line);
		if (line.length() < 2)
			break;

		for (short i = 0; i < line.length(); ++i)
			if (line[i] == ']')
				stacks[(i + 1)/4].push(line[i-1]);
	}

	for (short i = 0; i < N_STACKS; ++i) {
		while (!stacks[i].empty()) {
			invertor.push(stacks[i].top());
			stacks[i].pop();
		}

		while (!invertor.empty()) {
			stacks[i].push(invertor.front());
			invertor.pop();
		}
	}

	for (short i = 0; i < N_MOVES; ++i) {
		cin >> line >> n >> line >> a >> line >> b;

		--a; --b;
		while (n--) {
			tmp.push(stacks[a].top());
			stacks[a].pop();
		}

		while (!tmp.empty()) {
			stacks[b].push(tmp.top());
			tmp.pop();
		}
	}

	for (short i = 0; i < N_STACKS; ++i) {
		if (!stacks[i].empty())
			cout << stacks[i].top();
		else
			cout << " ";
	}
	cout << endl;

	return 0;
}
