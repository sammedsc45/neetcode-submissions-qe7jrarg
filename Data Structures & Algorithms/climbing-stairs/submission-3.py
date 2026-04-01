class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        
        # Initialize variables for (n-1)th and (n-2)th steps
        first = 1  # This represents ways(n-2)
        second = 2 # This represents ways(n-1)
        
        # Calculate ways from step 3 up to n
        for i in range(3, n + 1):
            current = first + second
            first = second
            second = current
            
        return second