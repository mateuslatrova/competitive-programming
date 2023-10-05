# Problem: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  44ms   / 21.34MB /  a few seconds ago

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        
        split = False
        curr_node = root

        while not split:
            if curr_node.val == p.val or curr_node.val == q.val:
                return curr_node

            min_val = min(p.val, q.val)
            max_val = max(p.val, q.val)

            if min_val < curr_node.val and max_val > curr_node.val:
                split = True
            elif min_val < curr_node.val and max_val < curr_node.val:
                curr_node = curr_node.left
            else:
                curr_node = curr_node.right
        
        return curr_node