class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Add the current subset to the set as a tuple
            result.add(tuple(path))
            # Iterate over the remaining elements
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])
                # Move on to the next element
                backtrack(i + 1, path)
                # Backtrack by removing the last element added
                path.pop()

        # Sort the array to ensure subsets are in non-decreasing order
        nums.sort()
        result = set()
        backtrack(0, [])
        # Convert each tuple back to a list and return the result as a list of lists
        return list(map(list, result))