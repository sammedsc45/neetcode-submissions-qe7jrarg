class Solution:
    def rob(self, nums: List[int]) -> int:
        # Initialize two variables:
        # rob1: the maximum amount robbed up to two houses back
        # rob2: the maximum amount robbed up to the previous house
        rob1, rob2 = 0, 0
        
        # Iterate over each house's money in the nums array
        for n in nums:
            # temp: the maximum amount we can rob if we rob this house (rob1 + n) 
            # or if we skip this house (rob2). We take the maximum of the two.
            temp = max(rob1 + n, rob2)
            
            # Update rob1 to be the previous rob2 (shift the window forward)
            rob1 = rob2
            
            # Update rob2 to be the current maximum amount (either rob this house or skip)
            rob2 = temp
        
        # After the loop, rob2 will hold the maximum amount that can be robbed
        return rob2