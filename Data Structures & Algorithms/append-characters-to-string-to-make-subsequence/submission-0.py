class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        #the frequency of letters in s that exist in t should == len(t)
        l, r = 0, 0

        while l < len(s) and r<len(t):
            if s[l] != t[r]:
                l+=1
            else:
                l+=1
                r+=1
        return (len(t) - r)




        