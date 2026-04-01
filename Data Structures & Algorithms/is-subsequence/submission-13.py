class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l, r = 0, 0
        while r < len(t):
            if l == len(s):
                return True
            if s[l] != t[r]:
                r+=1
            else:
                l+=1
                r+=1
        return l == len(s)