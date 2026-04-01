"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Step 1: Interleave the original list with copied nodes
        current = head
        while current:
            copy = Node(current.val)
            copy.next = current.next
            current.next = copy
            current = copy.next

        # Step 2: Assign random pointers to the copied nodes
        current = head
        while current:
            copy = current.next
            if current.random:
                copy.random = current.random.next
            current = copy.next

        # Step 3: Separate the copied list from the original list
        original = head
        copy_head = head.next
        copy = copy_head
        while original:
            original.next = original.next.next
            if copy.next:
                copy.next = copy.next.next
                copy = copy.next
            original = original.next
        
        return copy_head