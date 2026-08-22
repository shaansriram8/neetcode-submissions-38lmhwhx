class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        l, r = 0, 0
        maxseen = 0
        while r < len(s):
            if s[r] in seen:
                while s[r] in seen:
                    seen.remove(s[l])
                    l+=1
            else:
                seen.add(s[r])
                r+=1
                maxseen = max(maxseen, len(seen))
        return maxseen




        