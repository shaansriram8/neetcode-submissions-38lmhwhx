class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap = {}
        out = -1
        for ind, num in enumerate(s):
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for ind, char in enumerate(s):
            if hashmap[char] == 1:
                return ind
        return out

