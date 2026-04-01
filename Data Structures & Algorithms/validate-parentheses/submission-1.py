class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Dictionary to hold the pairs of brackets
        bracket_map = {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in bracket_map:
                # Check if stack is empty or top of stack is not the corresponding opening bracket
                top_element = stack.pop() if stack else '#'
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push onto stack
                stack.append(char)

        # Stack should be empty if all brackets are properly closed
        return not stack

# Time Complexity = O(n)