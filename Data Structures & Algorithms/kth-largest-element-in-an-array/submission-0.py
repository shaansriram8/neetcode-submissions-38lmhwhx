class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums] #maxheap
        heapq.heapify(heap) #heapfiy
        ctr = k
        while ctr != 0:
             x = heapq.heappop(heap)
             ctr = ctr-1
        return -x