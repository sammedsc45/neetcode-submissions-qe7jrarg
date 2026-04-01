class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sort_s = ''.join(sorted(s))
        sort_t = ''.join(sorted(t))
        if sort_s == sort_t:
            return True
        else:
            return False