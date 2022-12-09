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
 * --- Part Two ---
 *
 *  Content with the amount of tree cover available, the Elves just need to know
 *  the best spot to build their tree house: they would like to be able to see a
 *  lot of trees.
 *
 *  To measure the viewing distance from a given tree, look up, down, left, and
 *  right from that tree; stop if you reach an edge or at the first tree that is
 *  the same height or taller than the tree under consideration. (If a tree is
 *  right on the edge, at least one of its viewing distances will be zero.)
 *
 *  The Elves don't care about distant trees taller than those found by the
 *  rules above; the proposed tree house has large eaves to keep it dry, so they
 *  wouldn't be able to see higher than the tree house anyway.
 *
 *  In the example above, consider the middle 5 in the second row:
 *   30373
 *   25512
 *   65332
 *   33549
 *   35390
 *
 *  - Looking up, its view is not blocked; it can see 1 tree (of height 3).
 *  - Looking left, its view is blocked immediately; it can see only 1 tree (of
 *    height 5, right next to it).
 *  - Looking right, its view is not blocked; it can see 2 trees.
 *  - Looking down, its view is blocked eventually; it can see 2 trees (one of
 *    height 3, then the tree of height 5 that blocks its view).
 *
 *  A tree's scenic score is found by multiplying together its viewing distance
 *  in each of the four directions. For this tree, this is 4 (found by
 *  multiplying 1 * 1 * 2 * 2).
 *
 *  However, you can do even better: consider the tree of height 5 in the middle
 *  of the fourth row:
 *   30373
 *   25512
 *   65332
 *   33549
 *   35390
 *
 *  - Looking up, its view is blocked at 2 trees (by another tree with a height
 *    of 5).
 *  - Looking left, its view is not blocked; it can see 2 trees.
 *  - Looking down, its view is also not blocked; it can see 1 tree.
 *  - Looking right, its view is blocked at 2 trees (by a massive tree of
 *    height 9).
 *
 *  This tree's scenic score is 8 (2 * 2 * 1 * 2); this is the ideal spot for
 *  the tree house.
 *
 *  Consider each tree on your map. What is the highest scenic score possible
 *  for any tree?
 */

#define N_ROWS_COLS 	99

int main()
{
	short m[N_ROWS_COLS][N_ROWS_COLS];
	string line;
	short dist;
	unsigned long long best = 1, score;
	int k;

	for (int i = 0; i < N_ROWS_COLS; ++i) {
		cin >> line;
		for (int j = 0; j < line.length(); ++j)
			m[i][j] = line[j] - '0';
	}

	for (int i = 1; i < N_ROWS_COLS - 1; ++i) {
		for (int j = 1; j < N_ROWS_COLS - 1; ++j) {
			score = 1;
			for (k = 1; k <= i; ++k)
				if (m[i - k][j] >= m[i][j])
					break;
			k = k > i? i: k;
			score *= k;

			for (k = 1; k < N_ROWS_COLS - i; ++k)
				if (m[i + k][j] >= m[i][j])
					break;
			k = k == N_ROWS_COLS - i? N_ROWS_COLS - i - 1: k;
			score *= k;

			for (k = 1; k <= j; ++k)
				if (m[i][j - k] >= m[i][j])
					break;
			k = k > j? j: k;
			score *= k;

			for (k = 1; k < N_ROWS_COLS - j; ++k)
				if (m[i][j + k] >= m[i][j])
					break;
			k = k == N_ROWS_COLS - j? N_ROWS_COLS - j - 1: k;
			score *= k;

			best = score > best? score: best;
		}
	}

	cout << best << endl;

	return 0;
}
