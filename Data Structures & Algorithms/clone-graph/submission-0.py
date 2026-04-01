"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        old_to_new = {}  # Map original nodes to their clones

        def clone(node):
            # If the node has already been cloned, return it
            if node in old_to_new:
                return old_to_new[node]

            # Clone the node
            cloned_node = Node(node.val)
            old_to_new[node] = cloned_node

            # Clone the neighbors
            cloned_node.neighbors = [clone(neighbor) for neighbor in node.neighbors]

            return cloned_node

        return clone(node)