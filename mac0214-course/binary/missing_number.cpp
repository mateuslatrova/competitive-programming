// Problem: https://leetcode.com/problems/missing-number
// Status   / Language / Runtime / Memory  /  Time
// Accepted /    C++   / 7 ms    / 17.93 MB/ a few seconds ago

#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    int missingNumber(vector<int> &nums)
    {
        int n = nums.size();

        int expected_sum = n * (n + 1) / 2;

        int s = 0;
        for (auto num : nums)
            s += num;

        return expected_sum - s;
    }
};