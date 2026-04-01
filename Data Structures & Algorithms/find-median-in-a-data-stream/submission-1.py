class MedianFinder:

    def __init__(self):
        self.minheap = []
        self.maxheap = []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxheap, -num)

        # Step 2: Ensure ordering property
        if self.minheap and -self.maxheap[0] > self.minheap[0]:
            val = -heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, val)

        # Step 3: Rebalance sizes
        if len(self.maxheap) > len(self.minheap) + 1:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))

        if len(self.minheap) > len(self.maxheap):
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))

    def findMedian(self) -> float:
        ret = 0
        if self.minheap or self.maxheap:
            if len(self.maxheap) == len(self.minheap): #if of even values
                mid = -self.maxheap[0] + self.minheap[0]
                ret = mid / 2
            elif len(self.maxheap) > len(self.minheap): #if maxheap is bigger
                ret = -self.maxheap[0]
            elif self.minheap:
                ret = self.minheap[0]
        return ret

        #1->3->5
        #2->4
        
        