class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        
        l, r = 0, 0
        maxseen = 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                maxseen = max(maxseen, len(seen))
            else: 
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
        return maxseen
        