class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #heap that identifies most frequent task 
        #cooldown queue that enforces n-cycles
        freq = {}
        heap = []
        queue = deque()
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        for key, val in freq.items():
            heapq.heappush(heap, [-val, key])
        
        t = 0
        while heap or queue:
            t+=1
            if queue and t > queue[0][0]: #if n cycles have passed
                _, frequency, task = queue.popleft()
                heapq.heappush(heap, [frequency, task])
            if heap and -heap[0][0] > 0: #if there is a task available 
                frequency, task = heapq.heappop(heap) #process it
                frequency +=1 #decrement the frequency
                if frequency < 0:
                    queue.append((t+n, frequency, task))
        return t




