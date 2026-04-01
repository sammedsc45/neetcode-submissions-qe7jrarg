import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for n in nums:
            count[n] = 1 + count.get(n, 0)

        min_heap = []
        for num in count.keys():
            heapq.heappush(min_heap, (count[num], num))
            if len(min_heap)>k:
                heapq.heappop(min_heap)
        
        print(min_heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(min_heap)[1])
        return res