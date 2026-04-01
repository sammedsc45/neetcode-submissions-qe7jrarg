class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # Convert all stones to negative to simulate a max-heap
        stones = [-stone for stone in stones]
        
        # Create the max-heap
        heapq.heapify(stones)
        
        # Continue until there is at most one stone left
        while len(stones) > 1:
            # Pop the two largest stones
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            
            # If they are not equal, push the difference back into the heap
            if stone1 != stone2:
                heapq.heappush(stones, stone1 - stone2)
        
        # Return the last stone's weight (convert back to positive) or 0 if no stones left
        return -stones[0] if stones else 0