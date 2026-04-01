class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.arr = nums

    def add(self, val: int) -> int:
        self.arr.append(val)
        heapq.heapify(self.arr)
        for i in range(0, (len(self.arr)-self.k)):
            heapq.heappop(self.arr)
        return self.arr[0]

