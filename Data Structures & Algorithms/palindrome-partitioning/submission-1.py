class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub: str) -> bool:
            # Check if a substring is a palindrome
            return sub == sub[::-1]
        
        def backtrack(start: int, path: List[str]):
            # If we've reached the end of the string, add the current path to results
            if start == len(s):
                res.append(path[:])
                return
            
            # Explore all substrings starting from index `start`
            for end in range(start + 1, len(s) + 1):
                substring = s[start:end]
                # If the current substring is a palindrome, recurse with this substring included
                if is_palindrome(substring):
                    path.append(substring)
                    backtrack(end, path)
                    # Backtrack: remove the last added substring
                    path.pop()
        
        res = []
        backtrack(0, [])
        return res