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
 * --- Day 2: Rock Paper Scissors ---
 *  --- Part Two ---
 *  The Elf finishes helping with the tent and sneaks back over to you.
 *  "Anyway, the second column says how the round needs to end: X means you
 *  need to lose, Y means you need to end the round in a draw, and Z means you
 *  need to win. Good luck!"
 *
 *  The total score is still calculated in the same way, but now you need to
 *  figure out what shape to choose so the round ends as indicated. The example
 *  above now goes like this:
 *
 *  In the first round, your opponent will choose Rock (A), and you need the
 *  round to end in a draw (Y), so you also choose Rock. This gives you a score
 *  of 1 + 3 = 4.
 *  In the second round, your opponent will choose Paper (B), and you choose
 *  Rock so you lose (X) with a score of 1 + 0 = 1.
 *  In the third round, you will defeat your opponent's Scissors with Rock for
 *  a score of 1 + 6 = 7.
 *  Now that you're correctly decrypting the ultra top secret strategy guide,
 *  you would get a total score of 12.
 *
 *  Following the Elf's instructions for the second column, what would your
 *  total score be if everything goes exactly according to your strategy guide?
*/

unsigned short result(char op, char me)
{
	if (me == 'X')
		return (op + 2 - 'A')%3 + 1;
	else if (me == 'Y')
		return (op + 3 - 'A')%3 + 4;

	return (op + 4 - 'A')%3 + 7;
}

int main()
{
	unsigned int score = 0;
	char op, me;

	for (int i = 0; i < 2500; ++i) {
		cin >> op >> me;

		score += result(op, me);
	}

	cout << score << endl;

	return 0;
}
