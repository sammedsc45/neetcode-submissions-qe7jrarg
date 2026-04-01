class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Edge case: if the string is empty or has a single character, return the string itself
        if len(s) <= 1:
            return s
        
        # Function to expand around the center and return the longest palindrome
        def expand_around_center(left: int, right: int) -> str:
            # Expand as long as the characters are equal and the bounds are valid
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindrome substring (slice excludes the current left and right)
            return s[left + 1:right]
        
        longest_palindrome = ""
        
        # Iterate over each character and expand around both the center (single and double)
        for i in range(len(s)):
            # Odd-length palindromes (center is one character)
            palindrome1 = expand_around_center(i, i)
            # Even-length palindromes (center is between two characters)
            palindrome2 = expand_around_center(i, i + 1)
            
            # Update the longest palindrome if found a longer one
            longest_palindrome = max(longest_palindrome, palindrome1, palindrome2, key=len)
        
        return longest_palindrome