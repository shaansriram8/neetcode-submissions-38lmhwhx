class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        hashmap = {}

        out = ""

        for char in arr:
            hashmap[char] = hashmap.get(char, 0) + 1

        count = 0

        for char in arr:
            if hashmap[char] == 1: #if unique
                count = count + 1
                if count == k: 
                    out = char

        return out



        