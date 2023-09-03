# Problem: https://leetcode.com/problems/valid-anagram
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  56 ms / 16.74MB  /  a few seconds ago

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_frequencies = self.getCharacterFrequenciesFromWord(s)
        t_frequencies = self.getCharacterFrequenciesFromWord(t)

        if set(s_frequencies.keys()) != set(t_frequencies.keys()):
            return False
        
        is_anagram = True

        for char in s:
            if s_frequencies[char] != t_frequencies[char]:
                is_anagram = False
                break
        
        return is_anagram

    def getCharacterFrequenciesFromWord(self, word: str) -> dict:
        frequencies = {}

        for char in word:
            if char not in frequencies.keys():
                frequencies[char] = 1
            else:
                frequencies[char] += 1
        
        return frequencies