# https://leetcode.com/problems/binary-tree-maximum-path-sum

from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxpathsum = root.val
        self.recursion(root)
        return self.maxpathsum

    def recursion(self, node):

        if node is None:
            return 0
        
        left_maxpathsum = max(self.recursion(node.left), 0)
        right_maxpathsum = max(self.recursion(node.right), 0)

        split_path_sum = left_maxpathsum + node.val + right_maxpathsum
        self.maxpathsum = max(self.maxpathsum, split_path_sum)
        
        maxpathsum = node.val + max(left_maxpathsum, right_maxpathsum)

        return maxpathsum