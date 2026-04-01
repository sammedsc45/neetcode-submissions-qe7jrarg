class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        
        def backtrack(i, subset, curSum):
            # If the current sum equals the target, add the subset to the results
            if curSum == target:
                res.append(subset[:])
                return
            
            # If the current sum exceeds the target or if we've exhausted all elements, stop exploring
            if curSum > target or i >= len(nums):
                return
            
            # Option 1: Include nums[i] in the subset and recurse without moving to the next index
            subset.append(nums[i])
            backtrack(i, subset, curSum + nums[i])  # Stay at index `i` to allow reuse of the same element
            
            # Backtrack by removing the last added element
            subset.pop()
            
            # Option 2: Exclude nums[i] from the subset and move to the next index
            backtrack(i + 1, subset, curSum)
        
        # Start backtracking from the first index, with an empty subset and sum of 0
        backtrack(0, [], 0)
        return res