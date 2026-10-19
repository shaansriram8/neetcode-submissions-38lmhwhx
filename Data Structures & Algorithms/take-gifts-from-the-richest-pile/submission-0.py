class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        heap = []
        for gift in gifts:
            heapq.heappush(heap, -gift)
        
        t = 0
        while t < k:
            curr = -heapq.heappop(heap)
            curr = floor(sqrt(curr))
            heapq.heappush(heap, -curr)
            t+=1
        return -sum(heap)
        