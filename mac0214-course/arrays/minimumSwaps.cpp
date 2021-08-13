// Problem: https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

#include <bits/stdc++.h>

using namespace std;

// Complete the minimumSwaps function below.
int minimumSwaps(vector<int> arr) {

    int n = arr.size();
    int swaps = 0;

    int i = 0;
    while (i < n) {
        if (arr[i] == i+1) i++;
        else {
            swap(arr[i],arr[arr[i]-1]);
            swaps++;
        }
    }

    return swaps;
}