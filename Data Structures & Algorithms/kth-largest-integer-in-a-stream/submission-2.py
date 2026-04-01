class KthLargest:
    def __init__(self, k: int, nums: list):
        self.k = k
        # Initialize the min-heap with the elements of 'nums'
        self.minHeap = nums
        # Convert the list into a heap
        heapq.heapify(self.minHeap)
        
        # Reduce the heap size to 'k' by popping the smallest elements.
        # This ensures that only the 'k' largest elements remain in the heap.
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        # Push the new value into the heap
        heapq.heappush(self.minHeap, val)
        
        # If the heap grows larger than 'k', remove the smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # The smallest element in the heap (at index 0) is the kth largest element
        return self.minHeap[0]