
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq_map = Counter(nums)
        
        # Step 2: Use a max heap to get top k frequent elements
        # Python's heapq is a min-heap, so we use negative frequencies
        max_heap = [(-freq, num) for num, freq in freq_map.items()]
        heapq.heapify(max_heap)
        
        # Step 3: Extract top k elements
        result = [heapq.heappop(max_heap)[1] for _ in range(k)]

        return result
