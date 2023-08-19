# Problem: https://leetcode.com/problems/container-with-most-water
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  535 ms / 23.7 MB /  a few seconds ago


class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        n = len(height)
        l = 0
        r = n - 1
        max_area = 0

        while l < r:
            current_area = (r - l) * min(height[l], height[r])
            max_area = max(max_area, current_area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area


# Brute force approach:
# class Solution(object):
#     def maxArea(self, height):
#         """
#         :type height: List[int]
#         :rtype: int
#         """
#         n = len(height)
#         max_area = 0
#         for i, h in enumerate(height):
#             for j in range(i, n):
#                 current_area = (j-i) * min(height[i], height[j])
#                 max_area = max(max_area, current_area)

#         return max_area

# Testing:
if __name__ == "__main__":
    sol = Solution()
    sol.maxArea([1, 3, 2, 5, 25, 24, 5])
