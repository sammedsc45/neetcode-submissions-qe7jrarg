class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
       ch = set()
       left = 0
       max_len = 0
       for right in range(len(s)):
        while s[right] in ch:
            ch.remove(s[left])
            left+=1
        ch.add(s[right])
        max_len = max(max_len,right-left+1)
       return max_len

# Time Complexity = O(n)