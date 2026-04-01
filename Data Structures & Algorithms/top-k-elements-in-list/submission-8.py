class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        out = []
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            
        vals = []
        for keys, values in hashmap.items():
            vals.append((values, keys))
        vals.sort(reverse=True)
        print(vals)
        
        for i in range(k):
            out.append(vals[i][1])
        return out

