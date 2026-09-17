class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        out = []

        for point in points:
            x, y = point #[x1, y1]
            distance = math.sqrt((x - 0)**2 + (y - 0)**2) #distance
            print(distance)
            heapq.heappush(heap, (distance, [x, y])) #smallest distances pushed
            

        
        for i in range(k):
            val = heapq.heappop(heap) #pops smallest elements at top of heap
            distance = val[0] #distance
            x1, y1 = val[1] #x1, y1
            out.append([x1, y1])
        return out



        
        