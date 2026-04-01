# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance_and_height(node):
            if not node:
                return 0, True  # height is 0, and it's balanced
            
            left_height, left_balanced = check_balance_and_height(node.left)
            right_height, right_balanced = check_balance_and_height(node.right)
            
            # The tree is balanced if:
            # 1. Left subtree is balanced
            # 2. Right subtree is balanced
            # 3. The height difference between the left and right subtrees is no more than 1
            current_balanced = (left_balanced and
                                right_balanced and
                                abs(left_height - right_height) <= 1)
            
            # Height of the current node
            current_height = max(left_height, right_height) + 1
            
            return current_height, current_balanced
        
        _, is_balanced = check_balance_and_height(root)
        return is_balanced