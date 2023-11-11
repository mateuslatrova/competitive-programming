# https://leetcode.com/problems/longest-increasing-subsequence

from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        n = len(nums)
        dp = [1] * n
        maxlength = 1

        for i in range(n-1, -1, -1):
            
            for j in range(i+1, n):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

            if maxlength < dp[i]:
                maxlength = dp[i]

        return maxlength