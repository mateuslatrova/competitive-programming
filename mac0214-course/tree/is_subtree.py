# Problem: https://leetcode.com/problems/subtree-of-another-tree
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  130ms   / 13.90MB /  a few seconds ago

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: TreeNode
        :type subRoot: TreeNode
        :rtype: bool
        """
        self.possibleSubroots = []
        self.subRoot = subRoot

        self.findPossibleSubroots(root)

        for possibleSubroot in self.possibleSubroots:
            if self.compareNodesRecursively(possibleSubroot, self.subRoot):
                return True
        
        return False

    def findPossibleSubroots(self, root):
        
        if root is None:
            return

        if root.val == self.subRoot.val:
            self.possibleSubroots.append(root)
        
        self.findPossibleSubroots(root.left)
        self.findPossibleSubroots(root.right)


    def compareNodesRecursively(self, p, q):

        if (p is None and q is not None) or (p is not None and q is None): 
            self.is_same = False
            return False

        if p is None and q is None:
            return True

        if p.val != q.val:
            self.is_same = False
            return False
        
        return self.compareNodesRecursively(p.left, q.left) and self.compareNodesRecursively(p.right, q.right)
        