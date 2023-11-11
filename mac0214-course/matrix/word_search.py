
# https://leetcode.com/problems/word-search

from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        self.h = len(board)
        self.w = len(board[0])
        self.neighbors = [(1, 0),(-1, 0), (0, 1), (0, -1)]
        self.visited = set()

        for i in range(self.h):
            for j in range(self.w):
                if board[i][j][0] != word[0]:
                    continue

                if self.dfs(board, word, i, j, 0):
                    return True
                    
        return False       

    def dfs(self, board, word, i, j, k):
        if k == len(word):
            return True
        
        if (i,j) in self.visited:
            return False

        if i < 0 or i >= self.h or j < 0 or j >= self.w:
            return False

        if word[k] != board[i][j]:
            return False

        self.visited.add((i,j))

        results = []
        for ni, nj in self.neighbors:
            newi, newj = (i+ni, j+nj)
            res = self.dfs(board, word, newi, newj, k+1)
            results.append(res)

        self.visited.remove((i,j))
        return any(results)
        
