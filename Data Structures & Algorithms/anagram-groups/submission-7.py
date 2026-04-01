class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for wrd in strs:
            cnt = [0]*26
            for c in wrd:
                cnt[ord(c)-ord('a')] += 1
            res[tuple(cnt)].append(wrd)
        return list(res.values())