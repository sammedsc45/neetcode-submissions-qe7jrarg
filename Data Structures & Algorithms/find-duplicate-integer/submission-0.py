class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Initialize the slow and fast pointers
        slow = nums[0]
        fast = nums[0]
        
        # Phase 1: Find the intersection point of the two runners
        while True:
            slow = nums[slow]  # move slow by one step
            fast = nums[nums[fast]]  # move fast by two steps
            if slow == fast:
                break
        
        # Phase 2: Find the entrance to the cycle
        slow = nums[0]  # move slow to the start
        while slow != fast:
            slow = nums[slow]  # move slow by one step
            fast = nums[fast]  # move fast by one step
        
        return slow