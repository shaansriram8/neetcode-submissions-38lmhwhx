class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #within window of len(s1), check if frequencies of s1 match thsoe in the window

        if len(s1) > len(s2):
            return False

        mapping = [0] * 26
        searching = [0] * 26
        l, r = 0, len(s1)-1

        for char in s1:
            mapping[ord(char)-ord('a')] +=1
        
        for ind in range(len(s1)):
            searching[ord(s2[ind])-ord('a')]+=1
        
        while r < len(s2):
            if searching == mapping:
                return True
            searching[ord(s2[l])-ord('a')]-=1
            l+=1
            r+=1
            if r == len(s2):
                return searching == mapping
            searching[ord(s2[r])-ord('a')]+=1
        return False



