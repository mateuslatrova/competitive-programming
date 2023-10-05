# Problem: https://leetcode.com/problems/invert-binary-tree
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  17ms   / 13.18MB /  a few seconds ago

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        return self.invertTreeRecursive(root)

    def invertTreeRecursive(self, root):
        if root is None:
            return None
        
        left_child_subtree = self.invertTreeRecursive(root.left)
        right_child_subtree = self.invertTreeRecursive(root.right)

        aux_subtree = left_child_subtree

        root.left = root.right
        root.right = left_child_subtree

        return root