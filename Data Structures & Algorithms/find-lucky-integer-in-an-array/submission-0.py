class Solution:
    def findLucky(self, arr: List[int]) -> int:
        hashmap = {}

        for num in arr:
            hashmap[num] = hashmap.get(num, 0) + 1
        maxval = -1
        for key, val in hashmap.items():
            if key == val:
                maxval = max(maxval, val)
        return maxval

        