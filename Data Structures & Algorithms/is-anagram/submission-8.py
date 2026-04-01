class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        counts = [0] * 26
        for ch in s:
            counts[ord(ch) - ord('a')] += 1
        for ch in t:
            counts[ord(ch) - ord('a')] -= 1
            
        return all(c == 0 for c in counts)