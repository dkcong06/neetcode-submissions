class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l, r = 0, 0
        letters = set()
        res = 0
        while r < len(s):
            if s[r] not in letters:
                letters.add(s[r])
            else:
                if len(letters) > res:
                    res = len(letters)
                while s[l] != s[r]:
                    letters.remove(s[l])
                    l += 1
                letters.remove(s[l])
                l += 1
                letters.add(s[r])
            r += 1
        if len(letters) > res:
            return len(letters)
        return res
            
            
