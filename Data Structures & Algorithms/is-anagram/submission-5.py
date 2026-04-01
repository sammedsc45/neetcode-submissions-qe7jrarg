class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_alpha = [0]*26
        t_alpha = [0]*26

        for ch in s:
            s_alpha[ord(ch)-ord('a')] += 1
        
        for ch in t:
            t_alpha[ord(ch)-ord('a')] += 1
        
        return s_alpha==t_alpha