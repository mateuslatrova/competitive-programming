// Problem: https://leetcode.com/problems/reverse-bits
// Status   / Language / Runtime / Memory  /  Time
// Accepted /    C++   / 0 ms    / 6.1 MB  / a few seconds ago

class Solution
{
public:
    uint32_t reverseBits(uint32_t n)
    {

        uint32_t num_of_bits = 32;
        uint32_t ans = 0;

        for (int i = 0; i < num_of_bits; i++)
        {
            if ((n & (1 << i)) != 0)
                ans += (1 << (num_of_bits - i - 1));
        }

        return ans;
    }
};