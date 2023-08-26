# Problem: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   / 42 ms   / 16.4 MB / a few seconds ago


class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        n = len(nums)
        r = n - 1
        l = 0
        minimum = nums[0]

        while l <= r:
            if nums[r] > nums[l]:
                minimum = min(nums[l], minimum)
                break

            mid = (l + r) // 2
            minimum = min(nums[mid], minimum)

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return minimum
