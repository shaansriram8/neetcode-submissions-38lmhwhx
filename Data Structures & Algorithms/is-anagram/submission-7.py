class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        arr_s = [0] * 26
        arr_t = [0] * 26

        for c in s:
            arr_s[ord(c)-ord('a')] +=1
        for c in t:
            arr_t[ord(c)-ord('a')] +=1
        return arr_t == arr_s

        