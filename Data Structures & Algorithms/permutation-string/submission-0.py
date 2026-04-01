from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Base condition: if s1 is longer than s2, s2 cannot contain a permutation of s1
        if len(s1) > len(s2):
            return False
        
        # Create frequency counters for s1 and the first window of s2
        s1_count = Counter(s1)
        window_count = Counter(s2[:len(s1)])
        
        # Check if the initial window matches the frequency count of s1
        if s1_count == window_count:
            return True
        
        # Slide the window across s2
        for i in range(len(s1), len(s2)):
            # Add the new character to the window
            window_count[s2[i]] += 1
            # Remove the character that is no longer in the window
            window_count[s2[i - len(s1)]] -= 1
            # Remove the character count from the dictionary if it drops to 0
            if window_count[s2[i - len(s1)]] == 0:
                del window_count[s2[i - len(s1)]]
            
            # Check if the current window matches the frequency count of s1
            if s1_count == window_count:
                return True
        
        return False