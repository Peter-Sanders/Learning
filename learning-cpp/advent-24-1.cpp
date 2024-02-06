#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
using namespace std;


int main(void) {

	string file_name = "advent-storage/advent-24-1.txt";

	ifstream input_stream(file_name);

	if (!input_stream) cout << "file not found";

	string line;
	int res = 0;
	while(getline(input_stream, line)) {
		int len = line.size();
		string back = line;
		reverse(back.begin(), back.end());

		string first;
		string last;
		int num;
		for (int i = 0; i < len; i++) {
			if (isdigit(line[i])) {
				first = line[i];
			}
			if (isdigit(back[i])) {
				last = back[i];
			}
		}
		num = stoi(last+first);
		res = res + num;
	}

	cout << res;
	return 0;
}
