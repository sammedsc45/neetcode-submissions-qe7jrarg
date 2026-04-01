class Solution:
    def rob(self, nums: List[int]) -> int:
        # Edge case: if there's only one house, return its value
        if len(nums) == 1:
            return nums[0]
        
        # Helper function to solve the linear version of the house robber problem
        def rob_linear(houses: List[int]) -> int:
            rob1, rob2 = 0, 0
            for n in houses:
                new_rob = max(rob1 + n, rob2)
                rob1 = rob2
                rob2 = new_rob
            return rob2
        
        # Case 1: Rob houses excluding the first house
        rob_exclude_first = rob_linear(nums[1:])
        
        # Case 2: Rob houses excluding the last house
        rob_exclude_last = rob_linear(nums[:-1])
        
        # The result is the maximum between these two cases
        return max(rob_exclude_first, rob_exclude_last)