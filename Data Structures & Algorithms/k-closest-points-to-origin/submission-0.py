class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        x2, y2 = 0, 0
        output = [0] * k
        heap = []
        for point in points:
            x1, y1 = point
            dist = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
            pair = (dist, (x1, y1))
            heapq.heappush(heap, pair)

        for i in range(k):
            output[i] = heapq.heappop(heap)[1]
        return output