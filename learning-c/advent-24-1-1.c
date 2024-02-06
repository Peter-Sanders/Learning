#include <stdio.h>
#include <string.h>
#include <ctype.h>

int main() {
    char *filename = "advent-42-1.txt";
    FILE *fp = fopen(filename, "r");

    if (fp == NULL) {
        printf("oh jeez");
        return 1;
    }

    const unsigned MAX_LENGTH = 256;
    char forward[MAX_LENGTH];
    int len;
    int res = 0;

    while (fgets(forward, MAX_LENGTH, fp)) {
        char first[2];  // Allocate space for a digit
        char last[2];   // Allocate space for a digit

        len = strlen(forward);
        char backward[len];

        for (int i = 0; i < len / 2; i++) {
            int temp = forward[i];
            backward[i] = forward[len - i - 1];
            backward[len - i - 1] = temp;
        }

        for (int i = 0; i < len; i++) {
            int curr_val = forward[i];
            if (isdigit(curr_val)) {
                first[0] = curr_val;
                first[1] = '\0';  // Null-terminate the string
                break;
            }
        }

        for (int i = 0; i < len; i++) {
            int curr_val = backward[i];
            if (isdigit(curr_val)) {
                last[0] = curr_val;
                last[1] = '\0';  // Null-terminate the string
                break;
            }
        }

        strcat(first, last);  // Concatenate first and last
        int new_val = atoi(first);
        res = res + new_val;
    }

    fclose(fp);
    printf("Final Result: %d\n", res);

    return 0;
}

