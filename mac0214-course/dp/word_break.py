# https://leetcode.com/problems/word-break

from typing import List

class Solution:
    
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        
        dp = [False] * (len(s)+1)
        dp[len(s)] = True

        for i in range(len(s)-1, -1, -1):
            substring = s[i:]

            for word in wordDict:
                if substring.startswith(word):
                    dp[i] = dp[i] or dp[i + len(word)]
        
        return dp[0]

    # Failed tests:
    def wordBreakRecursive(self, s: str, wordDict: List[str]) -> bool:
        
        if s == "".join(["-"] * len(s)):
            return True
        
        results = []
        for word in wordDict:
            
            to_replace = "".join(["-"] * len(word))
            if word in s:
                t = s.replace(word, to_replace)
                res = self.wordBreakRecursive(t, wordDict)
            else:
                res = False

            results.append(res)

        return any(results)