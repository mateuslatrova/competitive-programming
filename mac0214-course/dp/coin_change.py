# https://leetcode.com/problems/coin-change

from typing import List

class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        
        self.max_value = amount + 1
        dp = [self.max_value] * (amount+1)
        dp[0] = 0

        for curr_amount in range(1, amount+1):
            
            for coin in coins:

                if coin > curr_amount:
                    continue
                
                if dp[curr_amount-coin] != -1:
                    dp[curr_amount] = min(dp[curr_amount], 1 + dp[curr_amount-coin])
            
            if dp[curr_amount] == self.max_value:
                dp[curr_amount] = -1
        
        return dp[amount]