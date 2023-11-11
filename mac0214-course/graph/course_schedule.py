# https://leetcode.com/problems/course-schedule

from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.v_to_e = {}

        for a, b in prerequisites:
            if a not in self.v_to_e:
                self.v_to_e[a] = []
            self.v_to_e[a].append(b)
        
        self.visited = set()
        for v in range(numCourses):
            result = self.dfs(v)

            if result == False:
                return result
        
        return True

    def dfs(self, v):
        if v in self.visited:
            # loop:
            return False

        if v not in self.v_to_e:
            return True

        self.visited.add(v)

        for neighbor in self.v_to_e[v]:
            res = self.dfs(neighbor)
            if not res:
                return False

        self.visited.remove(v)
        del self.v_to_e[v]

        return True