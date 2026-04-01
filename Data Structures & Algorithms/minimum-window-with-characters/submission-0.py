from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        # Dictionary to count characters in t
        dict_t = Counter(t)
        required = len(dict_t)  # Number of unique characters in t that need to be present in the window

        # Left and right pointer
        l, r = 0, 0

        # Formed is used to keep track of how many unique characters in t
        # are currently in the window in the desired frequency
        formed = 0

        # Dictionary to keep track of all the unique characters in the current window
        window_counts = defaultdict(int)

        # Result tuple (window length, left, right)
        ans = float("inf"), None, None

        while r < len(s):
            character = s[r]
            window_counts[character] += 1

            # If the frequency of the current character added matches the desired count in t
            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            # Try to contract the window until it ceases to be 'desirable'
            while l <= r and formed == required:
                character = s[l]

                # Save the smallest window and update the answer
                if r - l + 1 < ans[0]:
                    ans = (r - l + 1, l, r)

                # The character at the position pointed by l is no longer a part of the window
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1

                # Move left pointer ahead
                l += 1    

            # Keep expanding the right pointer
            r += 1    

        # Return the smallest window or an empty string if no such window exists
        return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]