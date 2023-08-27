// Problem: https://leetcode.com/problems/sum-of-two-integers
// Status   / Language / Runtime / Memory  /  Time
// Accepted /    C++   / 2 ms    / 5.9 MB  / a few seconds ago

class Solution
{
public:
    int getSum(int a, int b)
    {
        while (b != 0)
        {
            int aux = (a & b) << 1;
            a = a ^ b;
            b = aux;
        }
        return a;
    }
};