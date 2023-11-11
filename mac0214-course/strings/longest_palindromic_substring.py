# https://leetcode.com/problems/longest-palindromic-substring

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        self.palindrome = ""
        self.size = 0
        
        for i, c in enumerate(s):
            self.run(i, i)
            self.run(i, i+1)
        return self.palindrome

    def updateResult(self, palindrome, size):
        if size > self.size:
            self.size = size
            self.palindrome = palindrome

    def run(self, l, r):
        while l >= 0 and r < len(self.s) and self.s[l] == self.s[r]:
            self.updateResult(self.s[l:r+1], r-l+1)
            l -= 1
            r += 1