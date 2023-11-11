# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.rec(root, float("-inf"), float("inf"))

    def rec(self, node, minimum, maximum):

        if node is None:
            return True

        if minimum < node.val < maximum:
            ok = True    
        else:
            ok = False
        
        if not ok:
            return ok
        else:
            return ok and self.rec(node.left, minimum, node.val) and self.rec(node.right, node.val, maximum)