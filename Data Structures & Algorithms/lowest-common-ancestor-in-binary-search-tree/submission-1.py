# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Start from the root node of the BST
        while root:
            # If both p and q are smaller than root, then LCA must be in the left subtree
            if p.val < root.val and q.val < root.val:
                root = root.left
            # If both p and q are greater than root, then LCA must be in the right subtree
            elif p.val > root.val and q.val > root.val:
                root = root.right
            # We have found the split point, i.e., the LCA
            else:
                return root