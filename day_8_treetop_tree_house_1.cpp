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
 * --- Day 8: Treetop Tree House ---
 *
 *  The expedition comes across a peculiar patch of tall trees all planted
 *  carefully in a grid. The Elves explain that a previous expedition planted
 *  these trees as a reforestation effort. Now, they're curious if this would be
 *  a good location for a tree house.

First, determine whether there is enough tree cover here to keep a tree house hidden. To do this, you need to count the number of trees that are visible from outside the grid when looking directly along a row or column.

The Elves have already launched a quadcopter to generate a map with the height of each tree (your puzzle input). For example:

30373
25512
65332
33549
35390

Each tree is represented as a single digit whose value is its height, where 0 is the shortest and 9 is the tallest.

A tree is visible if all of the other trees between it and an edge of the grid are shorter than it. Only consider trees in the same row or column; that is, only look up, down, left, or right from any given tree.

All of the trees around the edge of the grid are visible - since they are already on the edge, there are no trees to block the view. In this example, that only leaves the interior nine trees to consider:

    The top-left 5 is visible from the left and top. (It isn't visible from the right or bottom since other trees of height 5 are in the way.)
    The top-middle 5 is visible from the top and right.
    The top-right 1 is not visible from any direction; for it to be visible, there would need to only be trees of height 0 between it and an edge.
    The left-middle 5 is visible, but only from the right.
    The center 3 is not visible from any direction; for it to be visible, there would need to be only trees of at most height 2 between it and an edge.
    The right-middle 3 is visible from the right.
    In the bottom row, the middle 5 is visible, but the 3 and 4 are not.

With 16 trees visible on the edge and another 5 visible in the interior, a total of 21 trees are visible in this arrangement.

Consider your map; how many trees are visible from outside the grid?

 */

#define N_ROWS_COLS 	99

int main()
{
	short m[N_ROWS_COLS][N_ROWS_COLS];
	bool v[N_ROWS_COLS][N_ROWS_COLS];
	string line;
	unsigned int visible = 0;
	short tallest;

	for (int i = 0; i < N_ROWS_COLS; ++i) {
		cin >> line;
		for (int j = 0; j < line.length(); ++j) {
			m[i][j] = line[j] - '0';
			v[i][j] = false;
		}
	}

	for (int i = 0; i < N_ROWS_COLS; ++i) {
		v[i][0] = true;
		tallest = m[i][0];
		for (int j = 1; j < N_ROWS_COLS; ++j) {
			v[i][j] |= m[i][j] > tallest;
			tallest = m[i][j] > tallest? m[i][j]: tallest;
			if (tallest == 9)
				break;
		}

		v[0][i] = true;
		tallest = m[0][i];
		for (int j = 1; j < N_ROWS_COLS; ++j) {
			v[j][i] |= m[j][i] > tallest;
			tallest = m[j][i] > tallest? m[j][i]: tallest;
			if (tallest == 9)
				break;
		}

		v[i][N_ROWS_COLS - 1] = true;
		tallest = m[i][N_ROWS_COLS - 1];
		for (int j = N_ROWS_COLS - 2; j >= 0; --j) {
			v[i][j] |= m[i][j] > tallest;
			tallest = m[i][j] > tallest? m[i][j]: tallest;
			if (tallest == 9)
				break;
		}

		v[N_ROWS_COLS - 1][i] = true;
		tallest = m[N_ROWS_COLS - 1][i];
		for (int j = N_ROWS_COLS - 2; j >= 0; --j) {
			v[j][i] |= m[j][i] > tallest;
			tallest = m[j][i] > tallest? m[j][i]: tallest;
			if (tallest == 9)
				break;
		}
	}

	for (int i = 0; i < N_ROWS_COLS; ++i)
		for (int j = 0; j < line.length(); ++j)
			visible += v[i][j];

	cout << visible << endl;

	return 0;
}
