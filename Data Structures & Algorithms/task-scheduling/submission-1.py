class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks:
            return 0
        heap = [] #(freq, task)
        cooldown = deque() #(freq, task, timer)
        freq = {}
        t = 0
        for task in tasks:
            freq[task] = freq.get(task, 0) + 1
        
        for key, val in freq.items():
            heapq.heappush(heap, (-val, key))
        
        while heap or cooldown:
            t+=1
            if cooldown: #if there is time remaining
                if t == cooldown[0][2] + n + 1:
                    freq, task, time = cooldown.popleft()
                    heapq.heappush(heap, (freq, task))
            if heap:
                frequency, curr_task = heapq.heappop(heap)
                frequency +=1
                if frequency < 0:
                    cooldown.append((frequency, curr_task, t))
        return t
            

                

            



        