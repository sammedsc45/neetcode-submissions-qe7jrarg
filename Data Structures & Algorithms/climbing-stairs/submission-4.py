class Solution:
    def climbStairs(self, n: int) -> int:
        # If n is 1, there's only one way to climb
        if n == 1:
            return 1
        
        # Initialize the base cases
        prev1, prev2 = 2, 1
        
        # Calculate the number of ways iteratively
        for i in range(3, n + 1):
            current = prev1 + prev2
            prev2 = prev1
            prev1 = current
        
        # Return the result for n steps
        return prev1 if n > 1 else prev2