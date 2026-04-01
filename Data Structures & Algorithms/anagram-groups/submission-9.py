class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            s_alpha = [0]*26
            for ch in s:
                s_alpha[ord("a")-ord(ch)]+=1
            res[tuple(s_alpha)].append(s)
        return list(res.values())