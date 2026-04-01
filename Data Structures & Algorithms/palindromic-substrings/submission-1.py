class Solution:
    def countSubstrings(self, s: str) -> int:
        # Function to expand around the center and count palindromic substrings
        def expand_around_center(left: int, right: int) -> int:
            count = 0
            # Expand while the characters at left and right are the same
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1  # Found a palindrome, increment the count
                left -= 1  # Move left pointer outward
                right += 1  # Move right pointer outward
            return count

        total_palindromes = 0
        
        # Iterate over each character and expand around it for both odd and even lengths
        for i in range(len(s)):
            # Odd-length palindromes (single center)
            total_palindromes += expand_around_center(i, i)
            # Even-length palindromes (center between two characters)
            total_palindromes += expand_around_center(i, i + 1)
        
        return total_palindromes