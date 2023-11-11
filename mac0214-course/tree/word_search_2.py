
# https://leetcode.com/problems/word-search-ii

import string
from typing import List

class Solution:

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        self.h = len(board)
        self.w = len(board[0])
        self.neighbors = [(1, 0),(-1, 0), (0, 1), (0, -1)]
        self.board = board
        self.words = words
        self.visited = set()
        self.results = set()

        self.trie = Trie()
        for word in words:
            self.trie.insert(word)

        for i in range(self.h):
            for j in range(self.w):
                self.dfs("", i, j)
                    
        return list(self.results)

    def dfs(self, word, i, j):
        
        if (i,j) in self.visited:
            return

        if i < 0 or i >= self.h or j < 0 or j >= self.w:
            return
        
        word += self.board[i][j]

        if not self.trie.startsWith(word):
            return
        
        self.visited.add((i,j))

        leaf_node = self.trie.search(word)

        if leaf_node is not None and leaf_node.eow:
            self.results.add(word)
            leaf_node.eow = False

        for ni, nj in self.neighbors:
            newi, newj = (i+ni, j+nj)
            self.dfs(word, newi, newj)

        self.visited.remove((i,j))

class Node:

    def __init__(self, char: str):
        self.char = char
        self.eow = False
        self.children = [None] * 26

class Trie:

    def __init__(self):
        self.root = Node(None)
        
        alphabet = string.ascii_lowercase

        self.char_to_index = {}
        for i, char in enumerate(alphabet):
            self.char_to_index[char] = i

    def insert(self, word: str) -> None:
        current_node = self.root

        for i, char in enumerate(word):
            alphabet_idx = self.char_to_index[char]
            child = current_node.children[alphabet_idx]

            if child is None:
                current_node.children[alphabet_idx] = Node(char)
            
            current_node = current_node.children[alphabet_idx]

            if i == len(word)-1:
                current_node.eow = True

    def search(self, word: str) -> bool:
        return self.searchRec(self.root, 0, word)
        
    def searchRec(self, node, index, word):
        if node is None:
            return False
        
        char = word[index]

        alphabet_idx = self.char_to_index[char]
        child = node.children[alphabet_idx]
        
        if index < len(word)-1:
            return self.searchRec(child, index+1, word)

        return child

    def startsWith(self, prefix: str) -> bool:
        return self.startsWithRec(self.root, 0, prefix)
        
    def startsWithRec(self, node, index, prefix):
        if node is None:
            return False
        
        char = prefix[index]

        alphabet_idx = self.char_to_index[char]
        child = node.children[alphabet_idx]
        
        if index < len(prefix)-1:
            return self.startsWithRec(child, index+1, prefix)

        if child is None:
            return False
        else:
            return True