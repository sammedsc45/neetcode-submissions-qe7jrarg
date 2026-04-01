class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case: If the input is empty, return an empty list
        if not digits:
            return []
        
        # Mapping of digits to letters according to the phone keypad
        digit_to_char = {
            '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
            '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
        }
        
        # Resultant list to hold all possible combinations
        res = []
        
        # Backtracking function to generate the letter combinations
        def backtrack(index: int, path: str):
            # If the current path length equals the length of digits, add it to the result
            if index == len(digits):
                res.append(path)
                return
            
            # Get the possible letters for the current digit
            possible_letters = digit_to_char[digits[index]]
            
            # Explore each letter mapped to the current digit
            for letter in possible_letters:
                backtrack(index + 1, path + letter)
        
        # Start the backtracking with an empty path and the first digit
        backtrack(0, "")
        return res