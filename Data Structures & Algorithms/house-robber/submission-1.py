class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: if no houses, return 0
        if not nums:
            return 0
        
        # Edge case: if only one house, return the amount of that house
        if len(nums) == 1:
            return nums[0]
        
        # Initialize the max amounts for the first two houses
        prev2 = 0   # Represents max amount we can rob from up to the house two steps back
        prev1 = nums[0]  # Represents max amount we can rob from up to the previous house
        
        # Iterate through the houses starting from the second house
        for i in range(1, len(nums)):
            # Calculate the current max amount
            current = max(prev1, prev2 + nums[i])
            
            # Update the previous two amounts for the next iteration
            prev2 = prev1
            prev1 = current
        
        # The final prev1 contains the maximum amount we can rob
        return prev1