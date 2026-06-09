class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(char for char in s if char.isalnum())
        s = s.lower()
        i, j = 0, len(s) - 1
        if i >= j:
            return True
        while s[i] == s[j]:
            if i >= j:
                return True
            i+=1
            j-=1
        return False
        