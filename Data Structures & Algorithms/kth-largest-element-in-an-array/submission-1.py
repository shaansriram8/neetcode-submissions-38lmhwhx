class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = [-n for n in nums] #maxheap
        heapq.heapify(heap) #heapfiy
        ctr = k
        while ctr != 0:
             x = heapq.heappop(heap)
             ctr = ctr-1
        return -x
        #class Solution:  more efficient
        
        #def findKthLargest(self, nums: List[int], k: int) -> int:
        #heap = []
        #for num in nums:
        #   heapq.heappush(heap, num)
         #   if len(heap) > k:
        #        heapq.heappop(heap)
        #return heap[0]