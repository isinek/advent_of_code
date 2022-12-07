#include <bits/stdc++.h>
#include <iostream>
#include <cstdlib>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>

#define dump(...)		cerr << "[" << #__VA_ARGS__ ": " << (__VA_ARGS__) << "]" << endl
#define arr_dump(...)		cerr << "[" << #__VA_ARGS__ "(" << sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]) << "): ["; for (unsigned long long int it = 0; it < sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]); ++it) cerr << (__VA_ARGS__)[it] << (it + 1 < sizeof((__VA_ARGS__))/sizeof((__VA_ARGS__)[0]) ? ", " : ""); cerr << "]]" << endl
#define vec_dump(...)		cerr << "[" << #__VA_ARGS__ "(" << (__VA_ARGS__).size() << "): ["; for (auto it = (__VA_ARGS__).begin(); it != (__VA_ARGS__).end(); ++it) cerr << *it << (it + 1 != (__VA_ARGS__).end() ? ", " : ""); cerr << "]]" << endl
#define pair_dump(...)		cerr << "[" << #__VA_ARGS__ ": (" << it->first << ", " << it->second << ")]" << endl
#define vec_pair_dump(...)	cerr << "[" << #__VA_ARGS__ "(" << (__VA_ARGS__).size() << "): ["; for (auto it = (__VA_ARGS__).begin(); it != (__VA_ARGS__).end(); ++it) cerr << "(" << it->first << ", " << it->second << ")" << (it + 1 != (__VA_ARGS__).end() ? ", " : ""); cerr << "]]" << endl

using namespace std;

/*
 * --- Day 7: No Space Left On Device ---
 *  You can hear birds chirping and raindrops hitting leaves as the expedition
 *  proceeds. Occasionally, you can even hear much louder sounds in the
 *  distance; how big do the animals get out here, anyway?
 *
 *  The device the Elves gave you has problems with more than just its
 *  communication system. You try to run a system update:
 *
 *  $ system-update --please --pretty-please-with-sugar-on-top
 *  Error: No space left on device
 *
 *  Perhaps you can delete some files to make space for the update?
 *
 *  You browse around the filesystem to assess the situation and save the
 *  resulting terminal output (your puzzle input). For example:
 *  $ cd /
 *  $ ls
 *  dir a
 *  14848514 b.txt
 *  8504156 c.dat
 *  dir d
 *  $ cd a
 *  $ ls
 *  dir e
 *  29116 f
 *  2557 g
 *  62596 h.lst
 *  $ cd e
 *  $ ls
 *  584 i
 *  $ cd ..
 *  $ cd ..
 *  $ cd d
 *  $ ls
 *  4060174 j
 *  8033020 d.log
 *  5626152 d.ext
 *  7214296 k
 *
 *  The filesystem consists of a tree of files (plain data) and directories
 *  (which can contain other directories or files). The outermost directory is
 *  called /. You can navigate around the filesystem, moving into or out of
 *  directories and listing the contents of the directory you're currently in.
 *
 *  Within the terminal output, lines that begin with $ are commands you
 *  executed, very much like some modern computers:
 *   - cd means change directory. This changes which directory is the current
 *     directory, but the specific result depends on the argument:
 *     - cd x moves in one level: it looks in the current directory for the
 *       directory named x and makes it the current directory.
 *     - cd .. moves out one level: it finds the directory that contains the
 *       current directory, then makes that directory the current directory.
 *     - cd / switches the current directory to the outermost directory, /.
 *   - ls means list. It prints out all of the files and directories immediately
 *     contained by the current directory:
 *     - 123 abc means that the current directory contains a file named abc with
 *       size 123.
 *     - dir xyz means that the current directory contains a directory named
 *       xyz.
 *
 *  Given the commands and output in the example above, you can determine that
 *  the filesystem looks visually like this:
 *   - / (dir)
 *     - a (dir)
 *       - e (dir)
 *         - i (file, size=584)
 *       - f (file, size=29116)
 *       - g (file, size=2557)
 *       - h.lst (file, size=62596)
 *     - b.txt (file, size=14848514)
 *     - c.dat (file, size=8504156)
 *     - d (dir)
 *       - j (file, size=4060174)
 *       - d.log (file, size=8033020)
 *       - d.ext (file, size=5626152)
 *       - k (file, size=7214296)
 *
 *  Here, there are four directories: / (the outermost directory), a and d
 *  (which are in /), and e (which is in a). These directories also contain
 *  files of various sizes.
 *
 *  Since the disk is full, your first step should probably be to find
 *  directories that are good candidates for deletion. To do this, you need to
 *  determine the total size of each directory. The total size of a directory is
 *  the sum of the sizes of the files it contains, directly or indirectly.
 *  (Directories themselves do not count as having any intrinsic size.)
 *
 *  The total sizes of the directories above can be found as follows:
 *   - The total size of directory e is 584 because it contains a single file i
 *     of size 584 and no other directories.
 *   - The directory a has total size 94853 because it contains files f (size
 *     29116), g (size 2557), and h.lst (size 62596), plus file i indirectly (a
 *     contains e which contains i).
 *   - Directory d has total size 24933642.
 *   - As the outermost directory, / contains every file. Its total size is
 *     48381165, the sum of the size of every file.
 *
 *  To begin, find all of the directories with a total size of at most 100000,
 *  then calculate the sum of their total sizes. In the example above, these
 *  directories are a and e; the sum of their total sizes is 95437
 *  (94853 + 584). (As in this example, this process can count files more than
 *  once!)
 *
 *  Find all of the directories with a total size of at most 100000. What is the
 *  sum of the total sizes of those directories?
 */

class Data
{
	private:
		string name;
		Data *parent;

	public:
		Data(Data *parent, string name) {
			this->parent = parent;
			this->name = name;
		}

		string getName() {
			return this->name;
		}

		Data* getParent() {
			return this->parent;
		}

		virtual unsigned long long getSize() {
			return 0;
		}

		virtual void printTree(unsigned short t) {
			for (short i = 0; i < t; ++i)
				cout << "  ";
			cout << this->name << endl;
		}
};

class File: public Data
{
	private:
		unsigned long long size;

	public:
		File(Data *parent, string name, unsigned long long size) : Data(parent, name) {
			this->size = size;
		}

		unsigned long long getSize() {
			return this->size;
		}

		void printTree(unsigned short t) {
			for (short i = 0; i < t; ++i)
				cout << "  ";
			cout << this->size << " " << this->getName() << endl;
		}
};

class Dir: public Data
{
	public:
		vector<Data *> data;

		Dir(Data *parent, string name) : Data(parent, name) {}

		unsigned long long getSize() {
			unsigned long long size = 0;

			for(auto d : this->data)
				size += d->getSize();

			return size;
		}

		void printTree(unsigned short t) {
			for (short i = 0; i < t; ++i)
				cout << "  ";
			cout << this->getName() << "  -> " << this->getSize() << endl;
			for (auto d : this->data)
				d->printTree(t + 1);
		}
};

int main()
{
	ifstream input_file("day_7_no_space_left_on_device.in");
	string line;
	Data *device = new Dir(NULL, "/");
	Dir *p = (Dir*)device;
	unsigned long long size;
	string filename;
	stack <Dir*> s;

	while (input_file) {
		getline(input_file, line);

		if (line == "$ ls") {
			continue;
		} else if (line == "$ cd /") {
			p = (Dir*)device;
		} else if (line == "$ cd ..") {
			p = (Dir*)p->getParent();
		} else if (line.substr(0, 5) == "$ cd ") {
			for (auto d : p->data) {
				if (d->getName() == line.substr(5)) {
					p = (Dir*)d;
					break;
				}
			}
		} else if (line.substr(0, 3) == "dir") {
			p->data.push_back(new Dir(p, line.substr(4)));
		} else {
			stringstream ss(line);
			ss >> size >> filename;

			p->data.push_back(new File(p, filename, size));
		}
	}

	// device->printTree(0);

	s.push((Dir*)device);
	size = 0;
	while (!s.empty()) {
		p = s.top();
		s.pop();

		if (p->getSize() < 100000)
			size += p->getSize();

		for (auto d : p->data) {
			if (Dir *next = dynamic_cast<Dir*>(d))
				s.push(next);
		}
	}

	cout << size << endl;

	return 0;
}
