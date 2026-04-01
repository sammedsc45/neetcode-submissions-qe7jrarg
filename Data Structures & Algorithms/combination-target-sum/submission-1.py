class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def backtrack(start, path, remaining):
            if remaining == 0:
                res.append(path[:])  # If we reach the target, add the current path to the results
                return
            if remaining < 0:
                return  # If we exceed the target, there's no need to continue

            for i in range(start, len(nums)):
                path.append(nums[i])  # Include the number in the combination
                # Because the same number can be reused, we pass 'i' instead of 'i + 1'
                backtrack(i, path, remaining - nums[i])
                path.pop()  # Backtrack to explore other combinations

        res = []
        backtrack(0, [], target)
        return res