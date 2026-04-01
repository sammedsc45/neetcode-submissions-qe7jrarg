''' Definition for singly-linked list.
 class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
'''
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node to act as the start of the result list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Traverse both linked lists
        while l1 or l2 or carry:
            # Get the current values from l1 and l2
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum of current digits plus carry
            total = val1 + val2 + carry
            
            # Update carry for next iteration
            carry = total // 10
            
            # Create a new node with the digit part of the sum
            current.next = ListNode(total % 10)
            
            # Move the current pointer
            current = current.next
            
            # Move to the next nodes in l1 and l2 if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        
        # Return the next node of dummy, which is the start of the actual result list
        return dummy.next