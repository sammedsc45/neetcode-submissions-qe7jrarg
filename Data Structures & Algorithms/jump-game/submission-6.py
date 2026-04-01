class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1  # Initialize goal to the last index
        for i in range(len(nums) - 1, -1, -1):  # Iterate from the last to the first index
            if i + nums[i] >= goal:  # If this position can reach the goal or beyond
                goal = i  # Update the goal to the current position
        return goal == 0  # If we can reach the first index, return True