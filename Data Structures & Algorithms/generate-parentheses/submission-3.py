class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(s=[], left=0, right=0):
            if len(s) == 2 * n:
                result.append("".join(s))
                return
            if left < n:
                backtrack(s + ['('], left + 1, right)  # Use list concatenation
            if right < left:
                backtrack(s + [')'], left, right + 1)  # Use list concatenation

        result = []
        backtrack()
        return result
