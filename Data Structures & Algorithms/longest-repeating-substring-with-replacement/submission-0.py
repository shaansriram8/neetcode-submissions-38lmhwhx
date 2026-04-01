class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        hashmap = {}
        max_char = 0
        res = 0
        while r < len(s):
            hashmap[s[r]] = hashmap.get(s[r], 0)+1 #freq counter
            max_char = max(max_char, hashmap[s[r]]) #return max character thus far in window
            
            while (r-l+1) - max_char > k:
                hashmap[s[l]] -=1
                l+=1
            res = max(res, r-l+1)
            r+=1
        return res
        


