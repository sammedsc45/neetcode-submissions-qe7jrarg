class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0  # Count the number of jumps
        l, r = 0, 0  # l and r are the bounds of the current window of reachable indices
        
        while r < len(nums) - 1:
            farthest = 0  # Track the farthest point we can reach in this window
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            
            # Move the window to the next range of reachable indices
            l = r + 1
            r = farthest
            
            # Increment the jump count
            res += 1
            
        return res