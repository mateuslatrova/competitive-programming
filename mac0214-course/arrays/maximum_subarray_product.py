# Problem: https://leetcode.com/problems/maximum-product-subarray
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  53 ms / 13.3 MB /  a few seconds ago


# Second try
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        current_min, current_max = 1, 1  # neutral value for multiplication
        max_product = -11  # -10 <= nums[i] <= 10

        for num in nums:
            if num == 0:
                current_min, current_max = 1, 1
                max_product = max(max_product, num)
                continue

            aux = num * current_max
            current_max = max([aux, num * current_min, num])
            current_min = min([aux, num * current_min, num])

            max_product = max(max_product, current_max)

        return max_product


# First try: Brute Force Solution
# It works, but I got a Time Limit Exceeded...
#
# class Solution(object):
#     def maxProduct(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: int
#         """
#
#         n = len(nums)
#         max_product = nums[0]
#         for i, num in enumerate(nums):
#             current_product = 1
#             for j in range(i, n):
#                 current_product *= nums[j]
#                 if current_product > max_product:
#                     max_product = current_product
#
#         return max_product
