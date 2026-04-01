import heapq

class KthLargest:
    def __init__(self, k: int, nums: list):
        """
        Initialize the class with 'k' and a list of integers 'nums'.
        'k' is the position of the largest element we want to track.
        'nums' is the stream of initial integers.

        We use a min-heap of size 'k' to efficiently track the kth largest element.
        """
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
        """
        Adds a new value to the stream and returns the kth largest element.
        If the heap size exceeds 'k', the smallest element is removed,
        maintaining the size of the heap at 'k'.
        """
        # Push the new value into the heap
        heapq.heappush(self.minHeap, val)
        
        # If the heap grows larger than 'k', remove the smallest element
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        
        # The smallest element in the heap (at index 0) is the kth largest element
        return self.minHeap[0]