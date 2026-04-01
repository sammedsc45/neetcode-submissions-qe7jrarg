from collections import defaultdict
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # Create a count of characters
            count = [0] * 26  # There are 26 letters in the English alphabet
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            # Convert list to tuple to use it as a key
            key = tuple(count)
            anagrams[key].append(word)

        return list(anagrams.values())