# Solution for problem: https://leetcode.com/problems/product-of-array-except-self/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        product = 1

        # Calculating prefix array (forward multiplication)
        prefix = [1]
        for i in range(n):
            product *= nums[i]
            prefix.append(product)
        prefix.append(1)
        
        # Calculating postfix array (backward multiplication)
        product = 1
        postfix = [1]
        for i in range(n):
            product *= nums[n-1-i]
            postfix.append(product)
        postfix.append(1)
        
        answer = []
        for i in range(1,n+1):
            answer.append(prefix[i-1] * postfix[n-i])

        return answer