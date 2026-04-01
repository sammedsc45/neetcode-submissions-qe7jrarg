class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start, path):
            # Append the current subset (path) to the result
            res.append(path[:])
            # Try to extend the subset with the remaining elements
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])
                # Recurse to add further elements
                backtrack(i + 1, path)
                # Backtrack to explore other subsets
                path.pop()
        
        res = []
        backtrack(0, [])
        return res