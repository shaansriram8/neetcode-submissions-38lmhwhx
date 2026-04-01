class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if s == "":
            return True
        
        j = 0
        for c in t:
            if j < len(s):
                if s[j] == c:
                    j+=1
            else:
                break
        
        if j == len(s):
            return True
        return False
            
        