class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        hashmap = {}
        for c in s:
            hashmap[c] = 0
        l, r = 0, 0
        maxseen = 0
        count = 0
        while r < len(s):
            hashmap[s[r]] += 1
            count = max(count, hashmap[s[r]])
            length = r-l+1
            if length - count > k:
                hashmap[s[l]] -= 1
                l+=1

            r+=1
            maxseen = max(maxseen, r-l)
            print(maxseen)       
        #A = 3
        #B = 2
        #len =
        

        return maxseen

                

        
        