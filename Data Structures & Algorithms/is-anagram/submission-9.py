class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sarr = [0] * 26
        tarr = [0] * 26

        for c in s:
            sarr[ord(c) - ord('a')] += 1
        for c in t:
            tarr[ord(c) - ord('a')] += 1
        print(tarr)
        print(sarr)
        return tarr == sarr
        