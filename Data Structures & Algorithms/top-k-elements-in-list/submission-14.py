class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        out = []
        minheap = []
        for num in nums:
            freq[num] = freq.get(num, 0) + 1
        
        for num, frequency in freq.items():
            heapq.heappush(minheap, [frequency, num])
            if len(minheap) > k:
                heapq.heappop(minheap)
        
        for freq, num in minheap:
            out.append(num)
        return out


        

        