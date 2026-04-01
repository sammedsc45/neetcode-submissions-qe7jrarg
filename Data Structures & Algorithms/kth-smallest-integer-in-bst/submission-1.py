# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Initialize a stack to simulate the in-order traversal
        stack = []
        current = root
        
        # Iterate until we find the kth smallest element
        while current or stack:
            # Traverse to the leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process the node at the top of the stack
            current = stack.pop()
            k -= 1
            
            # If the current count matches k, we've found the kth smallest element
            if k == 0:
                return current.val
            
            # Move to the right subtree
            current = current.right