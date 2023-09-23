# Problem: https://leetcode.com/problems/maximum-depth-of-binary-tree/
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  49ms   / 18.88MB /  a few seconds ago

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:

        self.max_depth = 0
        
        if root is None:
            return self.max_depth
        
        self.maxDepthRecursive(root, self.max_depth)
        
        return self.max_depth

    def maxDepthRecursive(self, node, parent_depth):
        if node is None:
            self.max_depth = max(parent_depth, self.max_depth)
            return
        
        current_depth = parent_depth + 1

        self.maxDepthRecursive(node.left, current_depth)
        self.maxDepthRecursive(node.right, current_depth)
