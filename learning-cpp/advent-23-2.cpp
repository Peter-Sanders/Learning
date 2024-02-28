#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <algorithm>
#include <boost/algorithm/string.hpp>
using namespace std;
using namespace boost;

int check_color(string color, string target_color, int color_count, string val){
	cout << color << val <<endl;
	if (color == target_color){
		color_count = color_count + stoi(val);
	}
	return color_count;
}


int main() {

	string file_name = "advent-storage/advent-23-2.txt";

	ifstream input_stream(file_name);

	if (!input_stream) {
		cout << "file not found";
		return 0;	
	}

	int redmax = 12;
	int greenmax= 13;
	int bluemax= 14;

	string line;
	int finalres = 0;
	while(getline(input_stream, line)) {
		int valid = 1;
		int len = line.size();
		int redcount, greencount, bluecount = 0;
		int end = line.find(":");
		string game = line.substr(0, end);
		int start = game.find(" ");
		string game_id = game.substr(start, len);
		/* cout << game_id + '\n'; */

		string rest = line.substr(end, len);
		int semi = rest.find(";");
		//cout << rest;
		while (semi != -1) {
			/* cout << rest.substr(0, semi) <<endl; */
			string res = rest.substr(0, semi);
			int comma = res.find(",");
			/* int reslen = res.size(); */
			while (comma != -1) {
				string result = res.substr(0, comma);
				int space = result.find(" ");
				int resultlen = result.size();
				while (space != -1) {
					string val = result.substr(0, space);
					string color = result.substr(space, resultlen);
					trim(color);

					redcount = check_color(color, "red", redcount, val);
					greencount = check_color(color, "green", greencount, val);
					bluecount = check_color(color, "blue", bluecount, val);
					/* if (color == "red") { */
					/* 	redcount = redcount + stoi(val); */
					/* } */
					/* if (color == "green") { */
					/* 	greencount = greencount + stoi(val); */
					/* } */
					/* if (color == "blue") { */
					/* 	bluecount = bluecount + stoi(val); */
					/* } */

					// continue the loop
					result.erase(result.begin(), result.begin() + space + 1);
					space = result.find(" ");
				}

				if (redcount > redmax || greencount > greenmax || bluecount > bluemax){
					valid = 0;
				}

				// continue the loop
				res.erase(res.begin(), res.begin() + comma + 1);
				comma = res.find(",");
			}

			// continue the loop
			rest.erase(rest.begin(), rest.begin() + semi + 1);
			semi = rest.find(";");

		}

		if (valid == 1) {
			/* cout << game_id + "\n"; */
			finalres = finalres + stoi(game_id);
		}

	}

	cout << finalres;
	cout << "\n";
	return 0;
}



