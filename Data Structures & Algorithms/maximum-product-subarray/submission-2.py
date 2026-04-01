class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Initialize the variables with the first element of the array
        max_so_far = min_so_far = global_max = nums[0]
        
        # Loop through the array starting from the second element
        for i in range(1, len(nums)):
            num = nums[i]
            
            # Since num can be negative, we swap max_so_far and min_so_far
            if num < 0:
                max_so_far, min_so_far = min_so_far, max_so_far
            
            # Update max_so_far and min_so_far
            max_so_far = max(num, max_so_far * num)
            min_so_far = min(num, min_so_far * num)
            
            # Update the global maximum product
            global_max = max(global_max, max_so_far)
        
        return global_max