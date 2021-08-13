// Problem: https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'hourglassSum' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts 2D_INTEGER_ARRAY arr as parameter.
 */

// Solution:
int hourglassSum(vector<vector<int>> arr) {
    // Idea: explore the center of each hourglass.

    vector<int> sums(16);

    int cnt = 0;
    for (int i = 1; i <= 4; i++) {
        for (int j = 1; j <= 4; j++) {
            sums[cnt] += arr[i][j];
            int up = i-1;
            int down = i+1;
            for (int col = j-1; col <= j+1; col++) {
                sums[cnt] += arr[up][col];
                sums[cnt] += arr[down][col];
            }
            cnt++;
        }
    }

    int max = sums[0];
    for (int i = 1; i < 16; i++) 
        if (max < sums[i]) max = sums[i];

    return max;
}