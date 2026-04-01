class Solution:
    def scoreOfString(self, s: str) -> int:
        l, r = 0, 1
        total = 0
        while r < len(s):
            total += abs(ord(s[r]) - ord(s[l]))
            l+=1
            r+=1
        return total