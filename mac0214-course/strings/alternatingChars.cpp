#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'alternatingCharacters' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */

int alternatingCharacters(string s) {
    int n = s.size();
    int numDels = 0;
    int i = 0;

    while (i < n) {
        if (s[i] == 'A') {
            int j = i+1;
            while (s[j] == 'A' && j < n) {
                numDels++;
                j++;
            }
            i = j;
            continue;
        } else {
            int j = i+1;
            while (s[j] == 'B' && j < n) {
                numDels++;
                j++;
            }
            i = j;
            continue;
        }
    }

    return numDels;
}