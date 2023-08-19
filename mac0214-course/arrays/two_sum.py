# Problem: https://leetcode.com/problems/two-sum/
# Status   / Language / Runtime / Memory  /  Time   
# Accepted / Python   /  367 ms / 14.2 MB /  a minute ago

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complement = {}

        for idx, num in enumerate(nums):
            if num in complement.keys():
                return [idx, complement[num]]
            else:
                complement[target-num] = idx