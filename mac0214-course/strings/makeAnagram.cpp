// Problem: https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'makeAnagram' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. STRING a
 *  2. STRING b
 */

int makeAnagram(string a, string b) {
    string alph = "abcdefghijklmnopqrstuvwxyz";
    map<char,int> freqa;
    map<char,int> freqb;
    int numDels = 0;

    for (char c: a) freqa[c]++;
    for (char c: b) freqb[c]++;

    for (char l: alph) {
        int diff = abs(freqa[l]-freqb[l]);
        numDels += diff;
    }

    return numDels;
}