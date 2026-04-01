class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        l, r = 0, 0
        out = ""
        while l < len(word1) and r < len(word2):
            out+=word1[l]
            out+=word2[r]
            l+=1
            r+=1
        if l < len(word1):
            out+=word1[l:len(word1)]
        elif r < len(word2):
            out+=word2[r:len(word2)]
        return out

        