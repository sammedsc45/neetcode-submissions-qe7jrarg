class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Initialize a variable to track the farthest position we can reach
        farthest = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If the current index exceeds the farthest reachable position, return False
            if i > farthest:
                return False
            
            # Update the farthest position we can reach from the current index
            farthest = max(farthest, i + nums[i])
            
            # If the farthest position is already greater than or equal to the last index, return True
            if farthest >= len(nums) - 1:
                return True
        
        # If we finish the loop, return True as we can reach the last index
        return True