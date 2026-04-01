class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        for c in range(len(s)-1, -1, -1):
            if s[c] != " ":
                cnt +=1
            elif cnt:
                break
        return cnt
            