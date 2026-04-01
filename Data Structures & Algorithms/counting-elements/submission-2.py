class Solution:
    def countElements(self, arr: List[int]) -> int:

        hashmap = {}
        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1
        out = 0
        for num in arr:
            if num+1 in hashmap:
                out += 1
        return out
        