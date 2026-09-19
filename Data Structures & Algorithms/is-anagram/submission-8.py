class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Smap, Tmap = {}, {}

        for c in s:
            Smap[c] = Smap.get(c, 0) + 1
        for c in t:
            Tmap[c] = Tmap.get(c, 0) + 1
        
        return Tmap == Smap
        