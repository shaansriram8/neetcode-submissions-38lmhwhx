class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        out = []

        for pairs in points:
            x, y = pairs[0], pairs[1]
            dist = math.sqrt((x - 0)**2 + (y - 0)**2)
            stored = (dist, [x, y])
            heapq.heappush(heap, stored)
        
        for _ in range(k):
            val = heapq.heappop(heap)[1]
            out.append(val)
        
        return out
        