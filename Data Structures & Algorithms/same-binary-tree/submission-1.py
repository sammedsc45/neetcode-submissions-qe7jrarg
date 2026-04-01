# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # Base case: both nodes are None
        if not p and not q:
            return True
        
        # If one of the nodes is None and the other isn't, the trees aren't the same
        if not p or not q:
            return False
        
        # If the values of the current nodes differ, the trees aren't the same
        if p.val != q.val:
            return False
        
        # Recursively check if the left and right subtrees are the same
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)