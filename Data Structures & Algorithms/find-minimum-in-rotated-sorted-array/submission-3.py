class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # Check if the middle element is greater than the rightmost element
            if nums[mid] > nums[right]:
                # Minimum must be in the right part
                left = mid + 1
            else:
                # Minimum must be in the left part or could be the mid element
                right = mid
        
        # At the end of the loop, left == right and pointing to the minimum element
        return nums[left]