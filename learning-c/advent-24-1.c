#include <stdio.h>
/* #include <stdlib.h> */
#include <string.h>
#include <ctype.h>

int main ()
{
	char *filename = "advent-42-1.txt";
	FILE *fp = fopen(filename, "r");

	if (fp ==NULL) {
		printf("oh jeez");
		return 1;
	}
	/* char ch; */
	const unsigned MAX_LENGTH = 256;
	char forward[MAX_LENGTH];
	int len;
	int res = 0;
	int calibrations[2];
	while (fgets(forward, MAX_LENGTH, fp)){
		char first[0];
		char last[0];
		len = strlen(forward);
		char backward[len];
		
		for (int i = 0; i<len/2;i++) {
			int temp = forward[i];
			backward[i] = forward[len-i-1];
			backward[len-i-1] = temp;
		}
		/* printf("%d\n", len); */
		/* printf("%s\n", forward); */
		/* printf("%s\n", backward); */

		for (int i = 0; i <= len; i++){ 
		 	int curr_val =forward[i]; 
			if (isdigit(curr_val)){
				/* calibrations[0] = curr_val; */
				first[0] = curr_val;
				break;
			} 
		}
		for (int i = 0; i <= len; i++){ 
			int curr_val =backward[i]; 
			if (isdigit(curr_val)){
				/* printf("%c\n", curr_val); */
				last[0] = curr_val;
				/* calibrations[1] = curr_val; */
				break;
			} 
		}

		/* char  first[50] = calibrations[0]; */
		/* char  last[50] = calibrations[1]; */
		/* char new = first; */
		/* strcat(new, last); */
		/* strcat(new, last); */
		printf("%s\n", first);
		/* printf("%s\n", last); */
		/* printf("%s\n", new); */

		int new = first - '0';

		res = res + new;
	}

	fclose(fp);
	printf("Final Result: %d\n", res); 

	return 0;	
}
