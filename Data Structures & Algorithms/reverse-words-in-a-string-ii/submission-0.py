class Solution:
    def reverseWords(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        l, r = 0, len(s)-1

        while l <= r:
            s[l], s[r] = s[r], s[l]
            l+=1
            r-=1

        l, r = 0, 0

        while r < len(s):
            while r < len(s) and s[r] != " ":
                r+=1
            if r > l:
                r-=1
            tmp = r+1
            while l<=r:
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1
            r, l = tmp, tmp
        return s
            
        
            
        