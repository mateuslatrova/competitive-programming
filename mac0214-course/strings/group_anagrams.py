# Problem: https://leetcode.com/problems/group-anagrams
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  101 ms / 19.44MB  /  a few seconds ago

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordered_anagram_to_all_anagrams = {}

        for st in strs:
            ordered_anagram = "".join(sorted(st))
            
            if ordered_anagram not in ordered_anagram_to_all_anagrams.keys():
                ordered_anagram_to_all_anagrams[ordered_anagram] = []
            
            ordered_anagram_to_all_anagrams[ordered_anagram].append(st)
        
        return list(ordered_anagram_to_all_anagrams.values())
