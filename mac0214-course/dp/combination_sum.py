
# https://leetcode.com/problems/combination-sum

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.combinations = []
        self.candidates = candidates
        self.target = target

        self.recursion(0, [], 0)

        return self.combinations

    def recursion(self, i, elems, curr_sum):

        if curr_sum == self.target:
            self.combinations.append(elems.copy())
            return

        if curr_sum > self.target or i >= len(self.candidates):
            return

        # Include candidates[i]
        elems.append(self.candidates[i])
        self.recursion(i, elems, curr_sum + self.candidates[i])

        # Not include candidates[i]
        elems.pop()
        self.recursion(i+1, elems, curr_sum)
