from collections import Counter
import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each element in the list
        count = Counter(nums)
        # Use a heap to get the k most frequent elements
        return heapq.nlargest(k, count.keys(), key=count.get)