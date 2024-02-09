#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <stdlib.h>

int main ()
{
	char *filename = "advent-storage/advent-24-1.txt";
	FILE *fp = fopen(filename, "r");
	if (fp ==NULL) {
		printf("advent file not found");
		return 1;
	}
	const unsigned MAX_LENGTH = 256;
	char str[MAX_LENGTH];
	int res = 0;
	while (fgets(str, MAX_LENGTH, fp)){
		int numDigits = 0;
		char digits[strlen(str)];
		for (int i = 0; i<= strlen(str); i++) {
			if (isdigit(str[i])) {
				digits[numDigits] = str[i];
				numDigits += 1;
			}
		}
		char cal[2] = {digits[0],digits[numDigits-1]}; 
		res += atoi(cal);
	}

	fclose(fp);
	printf("Final Result: %d\n", res); 
	return 0;	
}
