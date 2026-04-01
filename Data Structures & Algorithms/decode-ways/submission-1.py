class Solution:
    def numDecodings(self, s: str) -> int:
        # Edge case: If the string starts with '0', it cannot be decoded
        if not s or s[0] == '0':
            return 0

        # DP variables to track the current and previous results
        prev1, prev2 = 1, 1  # Initialize for base cases

        # Loop through the string
        for i in range(1, len(s)):
            current = 0
            
            # Check if the current character can be decoded as a single digit (1 to 9)
            if s[i] != '0':
                current = prev1

            # Check if the last two characters can form a valid two-digit number (10 to 26)
            if s[i - 1] == '1' or (s[i - 1] == '2' and s[i] <= '6'):
                current += prev2

            # Move to the next iteration, update prev1 and prev2
            prev2 = prev1
            prev1 = current

        return prev1