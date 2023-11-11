
# https://leetcode.com/problems/merge-intervals

from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()

        merged = []

        i = 0
        while i < len(intervals):

            new_interval = intervals[i]

            while i < len(intervals) - 1:
                next_interval = intervals[i+1]

                if next_interval[0] <= new_interval[1]:
                    new_interval[1] = max(new_interval[1], next_interval[1])
                    i += 1
                else:
                    break
            
            i += 1
            merged.append(new_interval)

        return merged