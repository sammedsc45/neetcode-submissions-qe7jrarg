# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # This variable will hold the maximum diameter found during the traversal
        self.diameter = 0
        
        def dfs(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            # Recursively find the depth of left and right subtrees
            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            
            # Update the diameter with the largest path through the current node
            self.diameter = max(self.diameter, left_depth + right_depth)
            
            # Return the depth of the current node
            return max(left_depth, right_depth) + 1
        
        # Start the DFS traversal from the root
        dfs(root)
        
        return self.diameter