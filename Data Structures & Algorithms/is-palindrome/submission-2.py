class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        while left < right:
            # Move the left pointer to the next alphanumeric character
            while left < right and not s[left].isalnum():
                left += 1
            # Move the right pointer to the previous alphanumeric character
            while left < right and not s[right].isalnum():
                right -= 1
            # Compare characters ignoring case
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

#Time Complexity = O(n)