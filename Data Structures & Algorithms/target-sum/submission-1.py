class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}  # Memoization dictionary to store previously computed results

        def backtrack(i, total):
            # Base case: when all numbers have been processed
            if i == len(nums):
                return 1 if total == target else 0  # Return 1 if the total matches the target
            
            # If the subproblem is already solved, return the cached result
            if (i, total) in dp:
                return dp[(i, total)]
            
            # Explore both adding and subtracting the current number
            add_ways = backtrack(i + 1, total + nums[i])  # Add nums[i] to the total
            subtract_ways = backtrack(i + 1, total - nums[i])  # Subtract nums[i] from the total
            
            # Store the result in the dp dictionary and return the total number of ways
            dp[(i, total)] = add_ways + subtract_ways
            return dp[(i, total)]
        
        # Start the backtracking process from index 0 and total 0
        return backtrack(0, 0)