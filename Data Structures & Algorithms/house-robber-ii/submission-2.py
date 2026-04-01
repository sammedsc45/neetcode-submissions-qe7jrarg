from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        def helper(start: int, end: int) -> int:
            rob1, rob2 = 0, 0
            for i in range(start, end):
                temp = max(rob1 + nums[i], rob2)
                rob1 = rob2
                rob2 = temp
            return rob2
        
        # We can choose to rob either from the first house to the second last one,
        # or from the second house to the last one.
        return max(helper(0, len(nums) - 1), helper(1, len(nums)))