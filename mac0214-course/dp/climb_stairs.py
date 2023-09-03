# Problem: https://leetcode.com/problems/valid-palindrome/
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  37 ms / 18.35 MB /  a few seconds ago

class Solution:
    
    N = 45

    def climbStairsDp(self, n: int) -> int:
        dp = [0] * (self.N+1)
        
        # Base case:
        dp[1] = 1
        dp[2] = 2
        
        # Recurrence:
        for i in range(3, self.N+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]

    def climbStairsRecursive(self, n: int) -> int:
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairsRecursive(n-1) + self.climbStairsRecursive(n-2)