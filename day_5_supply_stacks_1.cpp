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
 *  The expedition can depart as soon as the final supplies have been unloaded
 *  from the ships. Supplies are stored in stacks of marked crates, but because
 *  the needed supplies are buried under many other crates, the crates need to
 *  be rearranged.
 *
 *  The ship has a giant cargo crane capable of moving crates between stacks. To
 *  ensure none of the crates get crushed or fall over, the crane operator will
 *  rearrange them in a series of carefully-planned steps. After the crates are
 *  rearranged, the desired crates will be at the top of each stack.
 *
 *  The Elves don't want to interrupt the crane operator during this delicate
 *  procedure, but they forgot to ask her which crate will end up where, and
 *  they want to be ready to unload them as soon as possible so they can embark.
 *
 *  They do, however, have a drawing of the starting stacks of crates and the
 *  rearrangement procedure (your puzzle input). For example:
 *   [D]
 *   [N] [C]
 *   [Z] [M] [P]
 *    1   2   3
 *
 *   move 1 from 2 to 1
 *   move 3 from 1 to 3
 *   move 2 from 2 to 1
 *   move 1 from 1 to 2
 *
 *  In this example, there are three stacks of crates. Stack 1 contains two
 *  crates: crate Z is on the bottom, and crate N is on top. Stack 2 contains
 *  three crates; from bottom to top, they are crates M, C, and D. Finally,
 *  stack 3 contains a single crate, P.
 *
 *  Then, the rearrangement procedure is given. In each step of the procedure, a
 *  quantity of crates is moved from one stack to a different stack. In the
 *  first step of the above rearrangement procedure, one crate is moved from
 *  stack 2 to stack 1, resulting in this configuration:
 *   [D]
 *   [N] [C]
 *   [Z] [M] [P]
 *    1   2   3
 *
 *  In the second step, three crates are moved from stack 1 to stack 3. Crates
 *  are moved one at a time, so the first crate to be moved (D) ends up below
 *  the second and third crates:
 *          [Z]
 *          [N]
 *      [C] [D]
 *      [M] [P]
 *   1   2   3
 *
 *  Then, both crates are moved from stack 2 to stack 1. Again, because crates
 *  are moved one at a time, crate C ends up below crate M:
 *          [Z]
 *          [N]
 *  [M]     [D]
 *  [C]     [P]
 *   1   2   3
 *
 *  Finally, one crate is moved from stack 1 to stack 2:
 *          [Z]
 *          [N]
 *          [D]
 *  [C] [M] [P]
 *   1   2   3
 *
 *  The Elves just need to know which crate will end up on top of each stack; in
 *  this example, the top crates are C in stack 1, M in stack 2, and Z in stack
 *  3, so you should combine these together and give the Elves the message CMZ.
 *
 *  After the rearrangement procedure completes, what crate ends up on top of
 *  each stack?
 */

#define N_STACKS 		9
#define N_MOVES 		501
#define MAX_STACK_SIZE 	60

int main()
{
	stack<char> stacks[N_STACKS];
	stack<char> tmp[N_STACKS];
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
			stacks[b].push(stacks[a].top());
			stacks[a].pop();
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
