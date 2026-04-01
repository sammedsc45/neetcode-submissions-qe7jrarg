class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return [[""]]
        ana_map = defaultdict(list)
        for s in strs:
            charCount = [0]*26
            for c in s:
                charCount[ord(c)-ord('a')]+=1
            key = tuple(charCount)
            ana_map[key].append(s)
        return list(ana_map.values())
        
