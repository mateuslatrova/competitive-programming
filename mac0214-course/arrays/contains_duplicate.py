# Problem: https://leetcode.com/problems/contains-duplicate
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  448 ms / 27.5 MB /  a few seconds ago

from collections import defaultdict


class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        frequency = defaultdict(int)

        for num in nums:
            frequency[num] += 1
            if frequency[num] >= 2:
                return True

        return False
