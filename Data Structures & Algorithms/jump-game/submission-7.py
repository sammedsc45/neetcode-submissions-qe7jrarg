class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1  # Initialize goal to the last index
        
        # Iterate from the last to the first index
        for i in range(len(nums) - 1, -1, -1):
            # If this position can reach the goal or beyond
            if i + nums[i] >= goal:
                goal = i  # Update the goal to the current position
        # If we can reach the first index, return True
        return goal == 0