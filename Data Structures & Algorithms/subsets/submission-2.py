class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []      # This will store all the subsets
        subset = []   # Temporary list to store the current subset

        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())  # When all elements are considered, add the current subset to results
                return
            # Include nums[i] in the current subset
            subset.append(nums[i])
            dfs(i + 1)   # Recurse with the current element included
            # Exclude nums[i] from the current subset
            subset.pop()
            dfs(i + 1)   # Recurse with the current element excluded

        dfs(0)   # Start the recursion from the first element
        return res