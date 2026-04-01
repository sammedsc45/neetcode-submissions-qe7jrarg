class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1  # Initialize two pointers

        while l < r:  # Loop until the two pointers meet
            curSum = numbers[l] + numbers[r]  # Calculate the current sum

            if curSum > target:  # If current sum is greater than target, move right pointer to the left
                r -= 1
            elif curSum < target:  # If current sum is less than target, move left pointer to the right
                l += 1
            else:  # If current sum equals target, return the 1-based indices
                return [l + 1, r + 1]

# Time Complexity: O(n)
# Space Complexity: O(1)