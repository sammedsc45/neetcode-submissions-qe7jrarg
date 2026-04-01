class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Get the lengths of the input strings
        m, n = len(text1), len(text2)
        
        # Create a DP table with (m+1) x (n+1) size initialized to 0
        # dp[i][j] represents the length of the LCS between text1[0:i] and text2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Loop over each character in both strings
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # If characters match, increment the LCS length by 1 from the previous state (diagonal)
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    # Otherwise, take the maximum value from either the left or top cell (previous subproblems)
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        # The result is the length of the LCS found in dp[m][n]
        return dp[m][n]