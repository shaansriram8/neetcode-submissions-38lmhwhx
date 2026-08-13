class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        heap = []
        out = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1

        for key, val in freq.items():
            heapq.heappush(heap, (-val, key))
        
        for _ in range(k):
            out.append(heapq.heappop(heap)[1])
        return out

        
            
        
