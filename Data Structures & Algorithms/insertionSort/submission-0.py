# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        states = []
        for i in range(len(pairs)):
            current = pairs[i]
            j = i - 1
            while j >= 0 and pairs[j].key > current.key:
                pairs[j + 1] = pairs[j]
                j -= 1
            pairs[j + 1] = current
            # Capture the state of the list after each insertion
            states.append([Pair(pair.key, pair.value) for pair in pairs])
        return states