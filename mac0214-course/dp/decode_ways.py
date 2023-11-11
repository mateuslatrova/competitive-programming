# https://leetcode.com/problems/decode-ways

class Solution:
    def numDecodings(self, s: str) -> int:

        if not s:
            return 0

        dp = [0] * (len(s) + 1)
        dp[len(s)] = 1
        for i in range(len(s)-1, -1, -1):

            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] += dp[i+1]
                
                if i >= len(s) - 1:
                    continue
                
                this_and_next = int(s[i] + s[i+1])
                if this_and_next < 10 or this_and_next > 26:
                    continue

                dp[i] += dp[i+2]
        
        return dp[0]