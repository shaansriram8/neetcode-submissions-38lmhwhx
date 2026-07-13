class Solution:
    def reorganizeString(self, s: str) -> str:
        hashmap = {}
        n = len(s)
        out = ""
        heap, queue = [], deque() #queue is (freq, task, time)

        #gets frequency mapping of characters
        for c in s: 
            hashmap[c] = hashmap.get(c, 0) + 1
        maxseen = 0

        #impossibility check & populate heap
        for letter, freq in hashmap.items():
            maxseen = max(maxseen, freq)
            heapq.heappush(heap, (-freq, letter)) #sort by frequency

        if maxseen > (n + 1) // 2: 
            return out
        t = 0
        while heap or queue:
            t +=1
            if queue:
                if t == queue[0][2] + 2: #if available
                    freq, letter, time = queue.popleft()
                    heapq.heappush(heap, (freq, letter))
            if heap:
                freq, letter = heapq.heappop(heap)
                out += letter #append the letter
                print(out)
                freq +=1 #decrement frequency
                if freq < 0:
                    queue.append((freq, letter, t)) #if still remaining, push to queue
        return out

        
        



        