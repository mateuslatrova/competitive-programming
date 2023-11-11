# https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        return self.buildTreeRec(preorder, inorder)

    def buildTreeRec(self, preorder, inorder):

        if not preorder:
            return None

        root_val = preorder[0]
        root = TreeNode(root_val)  
        root_index = inorder.index(root_val)

        left_tree_size = root_index
        right_tree_size = len(inorder) - 1 - root_index
            
        left_subtree = self.buildTreeRec(preorder[1:1+left_tree_size], inorder[0:root_index])
        right_subtree = self.buildTreeRec(preorder[1+left_tree_size:], inorder[root_index+1:])

        root.left = left_subtree
        root.right = right_subtree

        return root