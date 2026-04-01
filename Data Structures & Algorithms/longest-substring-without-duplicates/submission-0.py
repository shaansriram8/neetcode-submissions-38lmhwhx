class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        l, r = 0, 0
        max_res = 0
        while r < len(s):
            while s[r] in charset:
                charset.remove(s[l])
                l+=1
            charset.add(s[r])
            res = r-l+1
            max_res = max(res, max_res)
            r+=1
        return max_res
            







            
        
        