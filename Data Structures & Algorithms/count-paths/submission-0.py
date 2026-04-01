class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a row to store the number of paths for each column in the last row
        row = [1] * n  # Since the bottom row has only one path (moving right)

        # Iterate from the second last row up to the first row
        for i in range(m - 1):
            newRow = [1] * n  # Initialize the new row, as the last column always has one path (moving down)
            
            # Update the number of paths for each column by summing the right and down paths
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]  # Paths from the right and from below
            
            # Move to the next row (shift the current row down)
            row = newRow
        
        # Return the number of ways to reach the top-left corner
        return row[0]