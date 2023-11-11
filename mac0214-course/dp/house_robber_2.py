# https://leetcode.com/problems/house-robber-ii/

from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        
        max_without_first = self.robForSlice(nums, 1, len(nums)-1)
        max_without_last = self.robForSlice(nums, 0, len(nums)-2)

        return max(max_without_first, max_without_last)
    
    def robForSlice(self, nums, left, right):
        nums_sliced = nums[left:right+1]
        
        n = len(nums_sliced)
        
        dp = [0] * (n+1)
        dp[1] = nums_sliced[0]
        
        for i in range(2, n+1):
            dp[i] = max(dp[i-2]+nums_sliced[i-1], dp[i-1])

        return dp[n]