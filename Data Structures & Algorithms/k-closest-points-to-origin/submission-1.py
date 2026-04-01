class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Min-heap to store all points with their squared distances
        min_heap = []
        
        # Compute the distance for each point and add it to the heap
        for x, y in points:
            dist = x**2 + y**2
            heapq.heappush(min_heap, (dist, [x, y]))
        
        # Extract the first k elements from the heap (k closest points)
        return [heapq.heappop(min_heap)[1] for _ in range(k)]