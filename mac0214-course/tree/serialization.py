# https://leetcode.com/problems/serialize-and-deserialize-binary-tree

# Definition for a binary tree node.

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        serial = ""

        if root is None:
            return serial

        queue = []
        queue.append(root)
 
        while queue:
 
            node = queue.pop(0)

            if node is None:
                serial += "None*"
            else:
                serial += str(node.val) + "*"
            
            if node is not None:
                queue.append(node.left)
                queue.append(node.right)
        
        return serial

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """

        vals = data.split("*")
        vals.pop() # remove empty string

        if not vals:
            return None
        

        root = TreeNode(int(vals.pop(0)))
        queue = []
        queue.append(root)

        while queue:
            node = queue.pop(0)

            leftval = vals.pop(0)
            rightval = vals.pop(0)

            leftval = None if leftval == "None" else int(leftval)
            rightval = None if rightval == "None" else int(rightval)

            if leftval is None:
                leftnode = None
            else:
                leftnode = TreeNode(int(leftval))
            
            if rightval is None:
                rightnode = None
            else:
                rightnode = TreeNode(int(rightval))

            node.left = leftnode
            node.right = rightnode

            if leftnode is not None:
                queue.append(leftnode)
            
            if rightnode is not None:
                queue.append(rightnode)
        
        return root