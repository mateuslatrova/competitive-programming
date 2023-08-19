# Problem: https://leetcode.com/problems/maximum-subarray
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  535 ms / 26.5 MB /  a few seconds ago


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        max_sum = -10001
        max_sums = [max_sum]

        for idx, num in enumerate(nums):
            if num > max_sums[idx] + num:
                max_sums.append(num)
            else:
                max_sums.append(max_sums[idx] + num)

        max_sum = max(max_sums)
        return max_sum
