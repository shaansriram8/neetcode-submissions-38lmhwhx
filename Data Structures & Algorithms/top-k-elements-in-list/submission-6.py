class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hashmap = {}
        heap = []
        out = []

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1

        for key, val in hashmap.items():
            heapq.heappush(heap, [-val, key])


        for _ in range(k):
            out.append(heapq.heappop(heap)[1])
        
        return out


        