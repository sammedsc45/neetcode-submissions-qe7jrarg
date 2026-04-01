class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Add the current subset to the result
            result.append(path[:])
            # Iterate over the remaining elements
            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Include nums[i] in the current subset
                path.append(nums[i])
                # Move on to the next element
                backtrack(i + 1, path)
                # Backtrack by removing the last element added
                path.pop()

        # Sort the array to handle duplicates easily
        nums.sort()
        result = []
        backtrack(0, [])
        return result