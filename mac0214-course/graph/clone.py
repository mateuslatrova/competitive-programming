# https://leetcode.com/problems/clone-graph

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:

    node_to_new_node = {}

    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        return self.dfs(node)

    def dfs(self, node):

        if node is None:
            return node

        if node in self.node_to_new_node:
            return self.node_to_new_node[node] 

        new_node = Node(node.val)
        self.node_to_new_node[node] = new_node

        new_neighbors = []
        for neighbor in node.neighbors:
            new_neighbors.append(self.dfs(neighbor))

        new_node.neighbors = new_neighbors

        return new_node