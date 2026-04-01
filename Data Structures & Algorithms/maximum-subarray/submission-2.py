class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize variables to track the maximum sum and current sum
        max_sum = nums[0]
        current_sum = nums[0]
        
        # Loop through the array starting from the second element
        for i in range(1, len(nums)):
            # Update the current_sum: either add the current element to the subarray
            # or start a new subarray from the current element
            current_sum = max(nums[i], current_sum + nums[i])
            
            # Update the max_sum if the current_sum is greater
            max_sum = max(max_sum, current_sum)
        
        # Return the maximum sum found
        return max_sum