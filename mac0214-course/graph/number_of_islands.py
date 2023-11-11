# https://leetcode.com/problems/number-of-islands

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        self.h = len(grid)
        self.w = len(grid[0])
        self.neighbors = [(1, 0),(-1, 0), (0, 1), (0, -1)]

        self.water = "0"
        self.land = "1"
        self.visited = set()
        self.num_of_islands = 0

        for i in range(self.h):
            for j in range(self.w):
                
                if grid[i][j] == self.water:
                    continue

                new_island = self.dfs(i ,j, grid)
                
                if new_island:
                    self.num_of_islands += 1
        
        return self.num_of_islands        

    def dfs(self, i, j, grid):
        
        nodes = []
        nodes.append((i, j))
        new_island = False

        while len(nodes) > 0:

            i, j = nodes.pop()

            if i < 0 or i == self.h or j < 0 or j == self.w:
                continue

            if (i,j) in self.visited or grid[i][j] == self.water:
                continue

            self.visited.add((i,j))
            
            if grid[i][j] == self.land:
                new_island = True

            for ni, nj in self.neighbors:
                newi, newj = (i+ni, j+nj)
                nodes.append((newi, newj))
        
        return new_island