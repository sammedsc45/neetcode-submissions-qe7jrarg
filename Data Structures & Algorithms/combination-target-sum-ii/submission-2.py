class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()  # Sort to handle duplicates and make it easier to skip them

        def backtrack(i, subset, current_sum):
            # If we reach the end of the list
            if i == len(candidates):
                # If the current subset's sum equals the target, add it to the result
                if current_sum == target:
                    res.append(subset[:])  # Use a copy of subset
                return
            
            # Include the current candidate in the subset
            subset.append(candidates[i])
            # Recur with the next index, including the current candidate's value in the sum
            backtrack(i + 1, subset, current_sum + candidates[i])
            # Backtrack: remove the last added candidate
            subset.pop()
            
            # Skip all the duplicates to avoid duplicate combinations
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            # Recur without including the current candidate in the subset
            backtrack(i + 1, subset, current_sum)

        # Start the backtracking with an empty subset and a sum of 0
        backtrack(0, [], 0)
        return res