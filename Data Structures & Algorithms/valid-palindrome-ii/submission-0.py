class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalin(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True

        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                return isPalin(s, l+1, r) or isPalin(s, l, r-1)
            l+=1
            r-=1
        return True
        