class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        '''
        You are given two strings s1 and s2.

        Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

        Both strings only contain lowercase letters.
        '''
        

        if len(s2) < len(s1):
            return False

        mapping = [0] * 26
        searching = [0] * 26
        l, r = 0, len(s1)-1
        #this gives us the frequency count of our sliding window
        for char in s1:
            mapping[ord(char)-ord('a')] +=1

        #prepopulate the first iteration of the window 
        for char in range(len(s1)):
            searching[ord(s2[char])-ord('a')] +=1
        while r < len(s2):
            if searching == mapping:
                return True
            searching[ord(s2[l]) - ord('a')] -=1
            l+=1
            r+=1
            if r == len(s2):
                return searching == mapping
            searching[ord(s2[r]) - ord('a')] +=1
        return False
        

        