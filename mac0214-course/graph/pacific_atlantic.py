# https://leetcode.com/problems/pacific-atlantic-water-flow

from typing import List
from queue import Queue

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        self.h = len(heights)
        self.w = len(heights[0])
        self.neighbors = [(1, 0),(-1, 0), (0, 1), (0, -1)]
        
        self.atl = set()
        self.pac = set()

        for i in range(self.h):
            self.dfs(i, 0, self.pac, heights)
            self.dfs(i, self.w-1, self.atl, heights)

        for j in range(self.w):
            self.dfs(0, j, self.pac, heights)
            self.dfs(self.h-1, j, self.atl, heights)

        both = []
        for i in range(self.h):
            for j in range(self.w):
                if (i,j) in self.pac and (i,j) in self.atl:
                    both.append([i, j])

        return both
        

    def dfs(self, i0, j0, visit, heights):
        
        nodes = Queue()
        nodes.put((i0, j0))
        prev_height = heights[i0][j0]

        while nodes.qsize() > 0:

            i, j = nodes.get()

            if (i,j) in visit:
                continue

            if i < 0 or i == self.h or j < 0 or j == self.w:
                continue
            
            if heights[i][j] < prev_height:
                continue

            visit.add((i,j))
            prev_height = heights[i][j]

            for ni, nj in self.neighbors:
                newi, newj = (i+ni, j+nj)
                nodes.put((newi, newj))