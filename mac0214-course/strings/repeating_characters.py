
# https://leetcode.com/problems/longest-substring-without-repeating-characters

from collections import defaultdict

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        left = right = 0
        self.char_to_count = defaultdict(int)
        self.max_length = 0

        while right < len(s):
            self.char_to_count[s[right]] += 1
            while self.char_to_count[s[right]] > 1: 
                self.char_to_count[s[left]] -= 1
                left += 1

            self.updateResult(right-left+1)
            right += 1
        
        return self.max_length
            
    def updateResult(self, length):
        self.max_length = length if length > self.max_length else self.max_length
