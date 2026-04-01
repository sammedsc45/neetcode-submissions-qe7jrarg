class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # This will store all the permutations
        result = []
        
        # Helper function for backtracking
        def backtrack(start=0):
            # If we've reached the end, we have a complete permutation
            if start == len(nums):
                result.append(nums[:])  # Add a copy of the current permutation
                return
            
            for i in range(start, len(nums)):
                # Swap the current element with the start element
                nums[start], nums[i] = nums[i], nums[start]
                
                # Continue to generate permutations with the next element
                backtrack(start + 1)
                
                # Swap back to revert the change for the next iteration
                nums[start], nums[i] = nums[i], nums[start]
        
        # Start the backtracking algorithm
        backtrack()
        return result