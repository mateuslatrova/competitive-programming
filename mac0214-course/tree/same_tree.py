# Problem: https://leetcode.com/problems/same-tree
# Status   / Language / Runtime / Memory  /  Time
# Accepted / Python   /  32ms   / 16.33MB /  a few seconds ago

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.compareNodesRecursively(p, q)
    
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
