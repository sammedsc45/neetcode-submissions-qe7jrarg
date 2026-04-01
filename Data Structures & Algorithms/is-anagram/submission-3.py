class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_cnt = [0]*26
        for c in s:
            s_cnt[ord(c)-ord('a')] += 1
        
        t_cnt = [0]*26
        for c in t:
            t_cnt[ord(c)-ord('a')] += 1
        
        return s_cnt == t_cnt