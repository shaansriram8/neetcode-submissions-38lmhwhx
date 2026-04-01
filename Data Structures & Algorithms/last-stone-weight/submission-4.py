class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = [-s for s in stones]
        heapq.heapify(heap)

        if len(heap) == 1:
            return -heap[0]
        while len(heap) > 1:
            x, y = -1*heapq.heappop(heap), -1*heapq.heappop(heap)
            if x != y:
                heapq.heappush(heap, -(x-y))
        if len(heap) < 1:
            return 0
        return -heap[0]
            
            
