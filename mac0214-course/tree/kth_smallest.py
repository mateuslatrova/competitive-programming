# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.inOrderTraversal(root, k)
        return self.kth

    def inOrderTraversal(self, node, k):
        if node is None:
            return
        
        self.inOrderTraversal(node.left, k)
        
        self.count += 1
        if self.count == k:
            self.kth = node.val 
        
        self.inOrderTraversal(node.right, k)