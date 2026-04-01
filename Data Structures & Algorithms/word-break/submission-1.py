class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Create a DP array to store whether the substring from index i to the end can be segmented
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: an empty string can always be segmented
        
        # Convert wordDict into a set for O(1) lookups
        wordSet = set(wordDict)

        # Iterate through the string from the last character to the first
        for i in range(len(s) - 1, -1, -1):
            # Check for each word in wordSet if it matches the substring starting at index i
            for w in wordSet:
                # Ensure the word can fit within the remaining substring from i
                if (i + len(w)) <= len(s) and s[i : i + len(w)] == w:
                    # If the word matches, check if the remaining substring can be segmented
                    dp[i] = dp[i + len(w)]
                # If dp[i] is True, break early as no further checks are needed
                if dp[i]:
                    break
        
        # Return True if the whole string can be segmented
        return dp[0]