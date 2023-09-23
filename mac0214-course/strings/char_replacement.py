# Problem: https://leetcode.com/problems/longest-repeating-character-replacement
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  87ms   / 16.48MB /  a few seconds ago


from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        char_to_count = defaultdict(int)

        l = 0
        r = 0
        max_length = 0
        str_length = len(s)
        s += "#"

        for r in range(str_length):

            char_to_count[s[r]] += 1
            max_count = max(char_to_count.values())
            substring_size = r-l+1

            need_to_replace = substring_size - max_count

            r += 1
            
            if need_to_replace <= k:
                found_valid = True
            else:
                found_valid = False
                char_to_count[s[l]] -= 1
                l += 1
                
            if found_valid:
                max_length = max(substring_size, max_length)
        
        return max_length
