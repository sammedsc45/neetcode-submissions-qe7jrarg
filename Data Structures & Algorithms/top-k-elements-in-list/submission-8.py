import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cont = Counter(nums)
        # Grab the k most common elements
        top_k = [element for element, _ in cont.most_common(k)]
        # Print the result
        print(top_k)
        return top_k