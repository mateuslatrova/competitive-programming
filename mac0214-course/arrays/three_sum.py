# Problem: https://leetcode.com/problems/3sum

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums.sort()
        triples = []
        previous_a = None

        for i in range(len(nums)-2):

            a = nums[i]

            if i > 0 and a == previous_a:
                continue

            previous_a = a

            l = i+1
            r = len(nums)-1

            while l < r:
                b = nums[l]
                c = nums[r]
                three_sum = (a + b + c)

                if three_sum > 0:
                    r -= 1
                elif three_sum < 0:
                    l += 1
                else:
                    triples.append((a, b, c))
                    l += 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1

        return triples

if __name__ == "__main__":
    print(Solution().threeSum([-1,0,1,2,-1,-4]))
    print(Solution().threeSum([1,-1,-1,0]))