from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Frequency dictionary to store the count of characters in the current window
        char_count = defaultdict(int)
        # Initialize the left pointer of the sliding window
        left = 0
        # Variable to store the maximum frequency of any single character in the current window
        max_freq = 0
        # Variable to store the maximum length of the substring
        max_length = 0

        # Iterate through the string with the right pointer
        for right in range(len(s)):
            # Increment the count of the current character
            char_count[s[right]] += 1
            # Update the maximum frequency of any single character in the current window
            max_freq = max(max_freq, char_count[s[right]])

            # Calculate the number of characters that need to be replaced
            window_length = right - left + 1
            if window_length - max_freq > k:
                # If more than k replacements are needed, shrink the window from the left
                char_count[s[left]] -= 1
                left += 1

            # Update the maximum length of the valid window
            max_length = max(max_length, right - left + 1)

        return max_length