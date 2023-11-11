# https://leetcode.com/problems/jump-game/

from typing import List

class Solution:

    # O(n): Greedy solution
    def canJump(self, nums: List[int]) -> bool:
        
        n = len(nums)
        goal_position = n-1
        i = goal_position

        while i >= 0:
            print(i)
            if i + nums[i] >= goal_position:
                goal_position = i
            i -= 1

        return goal_position == 0

    # O(n²): TLE
    def canJumpDp(self, nums: List[int]) -> bool:
        
        n = len(nums)

        dp = [False] * n
        dp[0] = True

        for i in range(1, n):
            
            can_jump = False

            for j in range(i):
                if j + nums[j] >= i and dp[j] == True:
                    can_jump = True
                    break
            
            dp[i] = can_jump

        return dp[n-1]