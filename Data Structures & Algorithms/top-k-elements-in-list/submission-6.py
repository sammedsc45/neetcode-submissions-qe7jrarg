class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frq = {}
        for n in nums:
            frq[n] = 1 + frq.get(n, 0)
        sorted_ele = sorted(frq.keys(), key=lambda x: frq[x], reverse=True)

        return sorted_ele[:k]
