// Problem: https://www.hackerrank.com/challenges/sock-merchant/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

#include <bits/stdc++.h>

using namespace std;

/*
 * Complete the 'sockMerchant' function below.
 *
 * The function is expected to return an INTEGER.
 * The function accepts following parameters:
 *  1. INTEGER n
 *  2. INTEGER_ARRAY ar
 */

// Solution:
int sockMerchant(int n, vector<int> ar) {
    vector<int> numOfSocks(101);
    
    for (int sock: ar) numOfSocks[sock]++;
    
    int numOfPairs = 0;
    
    for (int i = 1; i <= 100; i++) numOfPairs += numOfSocks[i] / 2;
    
    return numOfPairs;
}
