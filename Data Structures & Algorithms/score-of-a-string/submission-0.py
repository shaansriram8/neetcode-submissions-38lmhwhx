class Solution:
    def scoreOfString(self, s: str) -> int:
        
        running = 0
        for i in range(len(s)-1):
            running += abs(ord(s[i+1]) - ord(s[i]))
        
        return running


        
        