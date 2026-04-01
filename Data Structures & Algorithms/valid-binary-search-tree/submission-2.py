# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate(node, min_val, max_val):
            if not node:
                return True
            
            # The current node's value must be within the range defined by min_val and max_val
            if not (min_val < node.val < max_val):
                return False
            
            # Recursively validate the left and right subtrees
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        # Start with the whole range of valid values for a BST
        return validate(root, float('-inf'), float('inf'))