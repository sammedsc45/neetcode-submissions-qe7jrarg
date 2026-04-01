class Solution:
    def isPalindrome(self, s: str) -> bool:
        so = ''.join(char.lower() for char in s if char.isalnum())
        if so == so[::-1]:
            return True
        else:
            return False