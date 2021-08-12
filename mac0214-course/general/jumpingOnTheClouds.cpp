// Problem: https://www.hackerrank.com/challenges/jumping-on-the-clouds/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'jumpingOnClouds' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts INTEGER_ARRAY c as parameter.
 */

// Solution:
int jumpingOnClouds(vector<int> c) {
    int n = c.size(); // number of clouds
    int j = 0; // minimum number of jumps

    int i = 0; // index counter
    while (i < n-1) {
        if (c[i+2] == 0) {
            j++;
            i += 2;
        } else {
            j++;
            i++;
        }
    }

    return j;
}
