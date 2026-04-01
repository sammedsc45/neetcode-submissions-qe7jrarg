# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, max_val):
            if not node:
                return 0
            
            # Check if the current node is a "good" node
            good = 1 if node.val >= max_val else 0
            
            # Update the max value for the path
            max_val = max(max_val, node.val)
            
            # Continue DFS on the left and right children
            good += dfs(node.left, max_val)
            good += dfs(node.right, max_val)
            
            return good
        
        # Start DFS from the root with the root's value as the initial max value
        return dfs(root, root.val)