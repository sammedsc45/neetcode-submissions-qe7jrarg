class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()  # Step 1: Sort the array
        triplets = []  # This will store the result
        
        # Step 2: Iterate through the array
        for i in range(len(nums) - 2):
            # Skip duplicate elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            left, right = i + 1, len(nums) - 1  # Two-pointer initialization
            
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                
                if total == 0:
                    triplets.append([nums[i], nums[left], nums[right]])
                    
                    # Move the left pointer and skip duplicates
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Move the right pointer and skip duplicates
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return triplets