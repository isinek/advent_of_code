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
 * --- Day 6: Tuning Trouble ---
 * --- Part Two ---
 *
 *  Your device's communication system is correctly detecting packets, but still
 *  isn't working. It looks like it also needs to look for messages.
 *
 *  A start-of-message marker is just like a start-of-packet marker, except it
 *  consists of 14 distinct characters rather than 4.
 *
 *  Here are the first positions of start-of-message markers for all of the
 *  above examples:
 *    mjqjpqmgbljsphdztnvjfqwrcgsmlb: first marker after character 19
 *    bvwbjplbgvbhsrlpgdmjqwftvncz: first marker after character 23
 *    nppdvjthqldpwncqszvftbrmjlhg: first marker after character 23
 *    nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg: first marker after character 29
 *    zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw: first marker after character 26
 *
 *  How many characters need to be processed before the first start-of-message
 *  marker is detected?
 */

int main()
{
	string buffer;
	unsigned int start = 0, end = 0;
	bool duplicates;

	cin >> buffer;

	for (end = 0; end < buffer.length(); ++end) {
		duplicates = false;
		for (unsigned int j = start; j < end; ++j) {
			if (buffer[j] == buffer[end]) {
				start = j + 1;
				duplicates = true;
				break;
			}
		}
		if (!duplicates && end - start == 13)
			break;
	}

	cout << end + 1 << endl;

	return 0;
}
