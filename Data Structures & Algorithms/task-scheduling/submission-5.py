class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        hashmap = {}
        heap = []
        queue = deque()
        t = 0
        for task in tasks:
            hashmap[task] = hashmap.get(task, 0) + 1
        
        for task, freq in hashmap.items():
            heapq.heappush(heap, (-freq, task))
        
        while heap or queue: #while there are any tasks remaining
            t+=1    
            if queue and queue[0][1] < t: #cooldown for a task is done
                freq, cooldown, task = queue.popleft() 
                heapq.heappush(heap, (freq, task)) #move it back to the heap 
            if heap: #if no cooldown ready, go to next available task
                freq, task = heapq.heappop(heap)
                freq +=1 #decrement frequency
                if freq == 0: #if this task is done, dont add it to cooldown 
                    continue
                cooldown = t + n #cooldown is currtime + cooldown time
                queue.append((freq, cooldown, task)) #append this task to the queue
        return t
                
