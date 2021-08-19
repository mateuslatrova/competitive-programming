// Problem: https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'checkMagazine' function below.
 *
 * The function accepts following parameters:
 *  1. STRING_ARRAY magazine
 *  2. STRING_ARRAY note
 */

void checkMagazine(vector<string> magazine, vector<string> note) {
    int m = magazine.size();
    int n = note.size();

    map<string,int> magazineTable;
    for (string word: magazine) magazineTable[word]++;

    for (string word: note) {
        // If the word is in the magazine:
        if (magazineTable.count(word) > 0 && magazineTable[word] > 0) {
            magazineTable[word]--;
        } else {
            cout << "No";
            return;
        }
    }
    cout << "Yes";
}