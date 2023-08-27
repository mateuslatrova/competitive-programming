// Problem: https://leetcode.com/problems/number-of-1-bits
// Status   / Language / Runtime / Memory  /  Time
// Accepted /    C++   / 4 ms    / 6 MB    / a few seconds ago

class Solution
{
public:
    int hammingWeight(uint32_t n)
    {

        uint32_t num_of_bits = 32;
        uint32_t ans = 0;

        for (int i = 0; i < num_of_bits; i++)
        {
            if ((n & (1 << i)) != 0)
                ans++;
        }

        return ans;
    }
};