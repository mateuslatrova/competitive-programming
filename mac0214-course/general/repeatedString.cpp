// Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'repeatedString' function below.
 *
 * The function is expected to return a LONG_INTEGER.
 * The function accepts following parameters:
 *  1. STRING s
 *  2. LONG_INTEGER n
 */

// Solution:
long repeatedString(string s, long n) {
    // Idea: 
    // Let infS be the infinite string. 
    // First, we count the number of 'a's in s.
    // We will divide the substring infS[0:n]
    // into n//ss strings(which are s). This
    // way, we get the number of 'a's through 
    // a multiplication.
    // Then, we just add up the missing number
    // of 'a's in the remaining string, that is
    // a substring of s.

    // Ex.: s = abcac and n = 10
    // number of 'a's in s(nA): 2;
    // infS[0:n] = "abacabacab"
    // divided: abac  |  abac   |  ab
    //            1        2      remaining string
    // Now we just multiply nA*2 and add the 1 'a'
    // from the remaining string -> nA = 5.

    // Implementation:
    int ss = s.size(); // string size
    vector<int> indexA; // index of every 'a' in s.
    long nA = 0; // number of 'a's.

    // counting number of 'a's in the entire par
    for (int i = 0; i < ss; i++) 
        if (s[i] == 'a') nA++;

    nA = nA * (n/ss);

    int rss = n%ss; // size of remaining string;
    for (int i = 0; i < rss; i++) 
        if (s[i] == 'a') nA++;

    return nA;
}

