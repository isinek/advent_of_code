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
 *  You try contacting the Elves using your handheld device, but the river
 *  you're following must be too low to get a decent signal.
 *
 *  You ask the device for a heightmap of the surrounding area (your puzzle
 *  input). The heightmap shows the local area from above broken into a grid;
 *  the elevation of each square of the grid is given by a single lowercase
 *  letter, where a is the lowest elevation, b is the next-lowest, and so on up
 *  to the highest elevation, z.
 *
 *  Also included on the heightmap are marks for your current position (S) and
 *  the location that should get the best signal (E). Your current position (S)
 *  has elevation a, and the location that should get the best signal (E) has
 *  elevation z.
 *
 *  You'd like to reach E, but to save energy, you should do it in as few steps
 *  as possible. During each step, you can move exactly one square up, down,
 *  left, or right. To avoid needing to get out your climbing gear, the
 *  elevation of the destination square can be at most one higher than the
 *  elevation of your current square; that is, if your current elevation is m,
 *  you could step to elevation n, but not to elevation o. (This also means that
 *  the elevation of the destination square can be much lower than the elevation
 *  of your current square.)
 *
 *  For example:
 *    Sabqponm
 *    abcryxxl
 *    accszExk
 *    acctuvwj
 *    abdefghi
 *
 *  Here, you start in the top-left corner; your goal is near the middle. You
 *  could start by moving down or right, but eventually you'll need to head
 *  toward the e at the bottom. From there, you can spiral around to the goal:
 *    v..v<<<<
 *    >v.vv<<^
 *    .>vv>E^^
 *    ..v>>>^^
 *    ..>>>>>^
 *
 *  In the above diagram, the symbols indicate whether the path exits each
 *  square moving up (^), down (v), left (<), or right (>). The location that
 *  should get the best signal is still E, and . marks unvisited squares.
 *
 *  This path reaches the goal in 31 steps, the fewest possible.
 *
 *  What is the fewest steps required to move from your current position to the
 *  location that should get the best signal?
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
			if (m[i][j] == 'S') {
				pos.first = i;
				pos.second = j;
				tmp.first = pos;
				tmp.second = 0;
				q.push(tmp);
				m[i][j] = 'a' - 1;
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
