from collections import Counter
import heapq
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        frequency = {}
        for num in nums:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1
        
        # Step 2: Sort the elements based on their frequency in descending order
        sorted_elements = sorted(frequency.keys(), key=lambda x: frequency[x], reverse=True)
        
        # Step 3: Return the top k elements
        return sorted_elements[:k]