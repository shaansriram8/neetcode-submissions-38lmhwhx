import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        heap = []
        final = []

        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
        
        for num in hashmap:
            heapq.heappush(heap, (hashmap[num], num))
        
        for n in range(len(hashmap)-k):
            heapq.heappop(heap)
        
        while heap:
            final.append(heapq.heappop(heap)[1])
            
        return final
        

        

            