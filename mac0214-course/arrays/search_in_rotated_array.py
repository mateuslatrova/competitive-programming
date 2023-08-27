# Problem: https://leetcode.com/problems/search-in-rotated-sorted-array
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   / 42 ms   / 16.7 MB / a few seconds ago

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        r = n - 1
        l = 0
        ans = -1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == target:
                ans = mid
                break

            # ao menos uma das duas porções está ordenada.

            # se a da esquerda está ordenada:
            if nums[mid] >= nums[l]:  # metade a esquerda esta sorted
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1

            if nums[r] >= nums[mid]:  # metade a direita esta sorted
                if nums[mid] <= target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return ans
