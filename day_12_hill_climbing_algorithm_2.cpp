#include <bits/stdc++.h>
#include <iostream>
#include <cstdlib>
#include <string>
#include <vector>
#include <queue>
#include <algorithm>
#include <sstream>

#define dump(...)		cerr << "[" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "]" << endl
#define arr_dump(...)		cerr << "[" << #__VA_ARGS__ "(" << sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]) << "): ["; for (unsigned long long int it = 0; it < sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]); ++it) cerr << (__VA_ARGS__)[it] << (it + 1 < sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]) ? ", " : ""); cerr << "]]" << endl
#define vec_dump(...)		cerr << "[" << #__VA_ARGS__ "(" << (__VA_ARGS__).size() << "): ["; for (auto it = (__VA_ARGS__).begin(); it != (__VA_ARGS__).end(); ++it) cerr << *it << (it + 1 != (__VA_ARGS__).end() ? ", " : ""); cerr << "]]" << endl
#define pair_dump(...)		cerr << "[" << #__VA_ARGS__ ": (" << it->first << ", " << it->second << ")]" << endl
#define vec_pair_dump(...)	cerr << "[" << #__VA_ARGS__ "(" << (__VA_ARGS__).size() << "): ["; for (auto it = (__VA_ARGS__).begin(); it != (__VA_ARGS__).end(); ++it) cerr << "(" << it->first << ", " << it->second << ")" << (it + 1 != (__VA_ARGS__).end() ? ", " : ""); cerr << "]]" << endl

using namespace std;

/*
 * --- Day 12: Hill Climbing Algorithm ---
 * --- Part Two ---
 *  As you walk up the hill, you suspect that the Elves will want to turn this
 *  into a hiking trail. The beginning isn't very scenic, though; perhaps you
 *  can find a better starting point.
 *
 *  To maximize exercise while hiking, the trail should start as low as
 *  possible: elevation a. The goal is still the square marked E. However, the
 *  trail should still be direct, taking the fewest steps to reach its goal. So,
 *  you'll need to find the shortest path from any square at elevation a to the
 *  square marked E.
 *
 *  Again consider the example from above:
 *    Sabqponm
 *    abcryxxl
 *    accszExk
 *    acctuvwj
 *    abdefghi
 *
 *  Now, there are six choices for starting position (five marked a, plus the
 *  square marked S that counts as being at elevation a). If you start at the
 *  bottom-left square, you can reach the goal most quickly:
 *    ...v<<<<
 *    ...vv<<^
 *    ...v>E^^
 *    .>v>>>^^
 *    >^>>>>>^
 *
 *  This path reaches the goal in only 29 steps, the fewest possible.
 *
 *  What is the fewest steps required to move starting from any square with
 *  elevation a to the location that should get the best signal?
 */

#define N_ROWS 	41
#define N_COLS 	81

int main()
{
	char m[N_ROWS][N_COLS] = {0, };
	unsigned long long mn[N_ROWS][N_COLS] = {0, };
	string line;
	pair <short, short> pos, end;
	unsigned long long steps = 0;
	queue <pair <pair <short, short>, unsigned long long>> q;
	pair <pair <short, short>, unsigned long long> tmp;
	char last;

	for (short i = 0; i < N_ROWS; ++i) {
		cin >> line;
		for (short j = 0; j < N_COLS; ++j) {
			m[i][j] = line[j];
			if (m[i][j] == 'S' || m[i][j] == 'a') {
				pos.first = i;
				pos.second = j;
				tmp.first = pos;
				tmp.second = 0;
				q.push(tmp);
				m[i][j] = 'a';
			} else if (last < m[i][j]) {
				last = m[i][j];
			} else if (m[i][j] == 'E') {
				end.first = i;
				end.second = j;
			}
		}
	}

	while (!q.empty()) {
		tmp = q.front();
		pos = tmp.first;
		steps = tmp.second;
		q.pop();
		++tmp.second;

		if (pos.first - 1 >= 0 && (mn[pos.first - 1][pos.second] == 0 ||
				mn[pos.first - 1][pos.second] > steps + 1) &&
				(m[pos.first][pos.second] + 1 >= m[pos.first - 1][pos.second] ||
				m[pos.first][pos.second] == last)) {
			tmp.first.first = pos.first - 1;
			tmp.first.second = pos.second;
			q.push(tmp);
			mn[pos.first - 1][pos.second] = tmp.second;
		}
		if (pos.first + 1 < N_ROWS && (mn[pos.first + 1][pos.second] == 0 ||
				mn[pos.first + 1][pos.second] > steps + 1) &&
				(m[pos.first][pos.second] + 1 >= m[pos.first + 1][pos.second] ||
				m[pos.first][pos.second] == last)) {
			tmp.first.first = pos.first + 1;
			tmp.first.second = pos.second;
			q.push(tmp);
			mn[pos.first + 1][pos.second] = tmp.second;
		}
		if (pos.second - 1 >= 0 && (mn[pos.first][pos.second - 1] == 0 ||
				mn[pos.first][pos.second - 1] > steps + 1) &&
				(m[pos.first][pos.second] + 1 >= m[pos.first][pos.second - 1] ||
				m[pos.first][pos.second] == last)) {
			tmp.first.first = pos.first;
			tmp.first.second = pos.second - 1;
			q.push(tmp);
			mn[pos.first][pos.second - 1] = tmp.second;
		}
		if (pos.second + 1 < N_COLS && (mn[pos.first][pos.second + 1] == 0 ||
				mn[pos.first][pos.second + 1] > steps + 1) &&
				(m[pos.first][pos.second] + 1 >= m[pos.first][pos.second + 1] ||
				m[pos.first][pos.second] == last)) {
			tmp.first.first = pos.first;
			tmp.first.second = pos.second + 1;
			q.push(tmp);
			mn[pos.first][pos.second + 1] = tmp.second;
		}
	}

	cout << m[end.first][end.second] << ": " << mn[end.first][end.second] << endl;

	return 0;
}
