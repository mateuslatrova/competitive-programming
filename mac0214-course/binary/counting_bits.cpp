// Problem: https://leetcode.com/problems/counting-bits
// Status   / Language / Runtime / Memory  /  Time
// Accepted /    C++   / 3 ms    / 8.43 MB    / a few seconds ago

#include <bits/stdc++.h>

using namespace std;

class Solution
{
public:
    vector<int> countBits(int n)
    {

        vector<int> ans = {0};
        int offset = 1;
        int next_power = offset * 2;

        for (int i = 1; i <= n; i++)
        {
            if (i == next_power)
            {
                offset = next_power;
                next_power *= 2;
            }

            ans.push_back(1 + ans[i - offset]);
        }

        return ans;
    }
};