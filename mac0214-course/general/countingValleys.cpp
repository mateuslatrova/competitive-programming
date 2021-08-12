// Problem: https://www.hackerrank.com/challenges/counting-valleys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen

#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'countingValleys' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER steps
 *  2. STRING path
 */

// Solution:
int countingValleys(int steps, string path) {
    map<char,int> UD;
    UD.insert({'U',1});
    UD.insert({'D',-1});

    int h = 0; // current height
    bool iv = false; // inside valley
    int n = 0; // number of valleys

    for (char c: path) {
        h += UD[c];
        if (!iv && h < 0) iv = true;
        else if (iv && h >= 0) {
            iv = false;
            n++;
        }
    }

    return n;
}
