# https://leetcode.com/problems/palindromic-substrings

class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: str
        """
        self.s = s
        self.count = 0
        
        for i, c in enumerate(s):
            self.run(i, i)
            self.run(i, i+1)
        
        return self.count

    def run(self, l, r):
        while l >= 0 and r < len(self.s) and self.s[l] == self.s[r]:
            self.count += 1
            l -= 1
            r += 1