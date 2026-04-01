from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Count the frequency of each number
        frq = Counter(nums)
        
        # Use the most_common method to get the top k frequent elements
        most_common = frq.most_common(k)
        
        # Extract just the elements (not their counts)
        return [item[0] for item in most_common]
