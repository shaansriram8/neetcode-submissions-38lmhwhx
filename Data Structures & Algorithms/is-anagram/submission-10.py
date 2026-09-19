class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        sarr = [0] * 26
        tarr = [0] * 26

        for c in s:
            sarr[ord(c) - ord('a')] += 1
        for c in t:
            tarr[ord(c) - ord('a')] += 1
        return tarr == sarr
        