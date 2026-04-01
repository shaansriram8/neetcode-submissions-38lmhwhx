class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        l, r = 0, len(s)-1

        while r >= l:
            temp = s[r]
            s[r] = s[l]
            s[l] = temp
            r-=1
            l+=1
        return s
        
        