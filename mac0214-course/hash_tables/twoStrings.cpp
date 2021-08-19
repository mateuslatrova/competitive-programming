// Problem: https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen

#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'twoStrings' function below.
 *
 * The function is expected to return a STRING.
 * The function accepts following parameters:
 *  1. STRING s1
 *  2. STRING s2
 */

string twoStrings(string s1, string s2) {
    map<char,int> c1; // chars in s1
    map<char,int> c2; // chars in s2

    for (char c: s1) c1[c]++;
    for (char c: s2) c2[c]++;

    for (map<char,int>::iterator it = c1.begin(); it != c1.end(); it++) {
        if (c2.find(it->first) != c2.end()) {
            return "YES";
        }
    }
    return "NO";
}