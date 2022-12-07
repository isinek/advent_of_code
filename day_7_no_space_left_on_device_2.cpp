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
 * --- Part Two ---
 *  Now, you're ready to choose a directory to delete.
 *
 *  The total disk space available to the filesystem is 70000000. To run the
 *  update, you need unused space of at least 30000000. You need to find a
 *  directory you can delete that will free up enough space to run the update.
 *
 *  In the example above, the total size of the outermost directory (and thus
 *  the total amount of used space) is 48381165; this means that the size of the
 *  unused space must currently be 21618835, which isn't quite the 30000000
 *  required by the update. Therefore, the update still requires a directory
 *  with total size of at least 8381165 to be deleted before it can run.
 *
 *  To achieve this, you have the following options:
 *   - Delete directory e, which would increase unused space by 584.
 *   - Delete directory a, which would increase unused space by 94853.
 *   - Delete directory d, which would increase unused space by 24933642.
 *   - Delete directory /, which would increase unused space by 48381165.
 *
 *  Directories e and a are both too small; deleting them would not free up
 *  enough space. However, directories d and / are both big enough! Between
 *  these, choose the smallest: d, increasing unused space by 24933642.
 *
 *  Find the smallest directory that, if deleted, would free up enough space on
 *  the filesystem to run the update. What is the total size of that directory?
 */

#define DISK_SIZE 		70000000
#define NEEDED_SPACE 	30000000

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

bool compareDirs(Dir *a, Dir *b) {
	return a->getSize() < b->getSize();
}

int main()
{
	ifstream input_file("day_7_no_space_left_on_device.in");
	string line;
	Data *device = new Dir(NULL, "/");
	Dir *p = (Dir*)device;
	unsigned long long size;
	string filename;
	stack <Dir*> s;
	vector <Dir*> candidates;

	while (!input_file.eof()) {
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
		} else if (line.length() > 2){
			stringstream ss(line);
			ss >> size >> filename;

			p->data.push_back(new File(p, filename, size));
		}
	}

	// device->printTree(0);

	s.push((Dir*)device);
	size = DISK_SIZE - device->getSize();
	while (!s.empty()) {
		p = s.top();
		s.pop();

		if (p->getSize() + size >= NEEDED_SPACE)
			candidates.push_back(p);

		for (auto d : p->data) {
			if (Dir *next = dynamic_cast<Dir*>(d))
				s.push(next);
		}
	}

	sort(candidates.begin(), candidates.end(), compareDirs);

	cout << candidates[0]->getSize() << endl;

	return 0;
}
