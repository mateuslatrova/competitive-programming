// Problem: https://www.hackerrank.com/challenges/special-palindrome-again/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings&h_r=next-challenge&h_v=zen

#include <bits/stdc++.h>

using namespace std;

bool isSpecial(int n, string s) {
    char c = s[0];
    for (int i = 0; i < n/2; i++)
        if (s[i] != c || s[i] != s[n-i-1]) return false;
    return true;
}

// Complete the substrCount function below.
long substrCount(int n, string s) {
    int numSpecial = n; // number of special substrings in s.
                     // initialized with n because all substrings
                     // of size 1(each character) is special.

    for (int i = 2; i < n; i++) {
        for (int j = 0; j < n-i+1; j++) { // j = size of the current analyzed substring.
            if (isSpecial(i,s.substr(j,i))) numSpecial++; 
        }
    }

    return numSpecial;
}