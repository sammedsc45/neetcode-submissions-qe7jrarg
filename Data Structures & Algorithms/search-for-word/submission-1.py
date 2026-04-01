class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # Get the number of rows and columns in the board
        rows, cols = len(board), len(board[0])
        
        # Create a visited matrix to keep track of visited cells
        visited = [[False] * cols for _ in range(rows)]

        # Define a Depth-First Search (DFS) helper function
        def dfs(r, c, i):
            # If we've reached the end of the word, return True
            if i == len(word):
                return True
            
            # If the current cell is out of bounds, visited, or doesn't match the word, return False
            if r < 0 or r >= rows or c < 0 or c >= cols or visited[r][c] or board[r][c] != word[i]:
                return False
            
            # Mark the current cell as visited
            visited[r][c] = True
            
            # Explore neighboring cells (up, down, left, right)
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                # If the word is found in a neighboring cell, return True
                if dfs(r + dr, c + dc, i + 1):
                    return True
            
            # If no match is found, unmark the current cell and return False
            visited[r][c] = False
            return False

        # Iterate over all cells in the board to find a starting point for the word
        for r in range(rows):
            for c in range(cols):
                # If the word is found starting from the current cell, return True
                if dfs(r, c, 0):
                    return True
        
        # If no match is found after exploring all cells, return False
        return False