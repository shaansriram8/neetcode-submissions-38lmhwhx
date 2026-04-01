class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        cnt = 0
        flag = True
        for c in range(len(s)-1, -1, -1):
            if s[c] != " " and flag:
                cnt +=1
            elif cnt and flag:
                flag = False
        return cnt
            