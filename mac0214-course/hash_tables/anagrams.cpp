// Problem: https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'sherlockAndAnagrams' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts STRING s as parameter.
 */


int sherlockAndAnagrams(string s) {
    int n = s.size();
    int numPairs = 0;

    for (int i = 1; i < n; i++) {
        vector<string> sameSizeSubs;
        for (int j = 0; j < n-i+1; j++) {
            string substring = s.substr(j,i);
            sort(substring.begin(),substring.end());
            sameSizeSubs.push_back(substring);
        }
        int m = sameSizeSubs.size();
        for (int j = 0; j < m; j++) {
            for (int k = j+1; k < m; k++) {
                if (sameSizeSubs[j]==sameSizeSubs[k]) numPairs++;
            }
        }
    }

    return numPairs;
}