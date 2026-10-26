class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        #Store (frequency, character) in maxheap
        #always try to get rid of most frequent character. 
        #have checks that prevent triples

        heap = []
        res = ""
        if a > 0:
            heapq.heappush(heap, (-a, 'a'))
        if b > 0:
            heapq.heappush(heap, (-b, 'b'))
        if c > 0:
            heapq.heappush(heap, (-c, 'c'))
        while heap:
            #triple prevention check
            if len(res) > 1 and res[-1] == heap[0][1] and res[-2] == heap[0][1]:
                if len(heap) > 1:
                    skipped = heapq.heappop(heap)
                    freq, char = heapq.heappop(heap)
                    res += char
                    freq +=1
                    if freq == 0:
                        heapq.heappush(heap, skipped)
                        continue
                    heapq.heappush(heap, (freq, char))
                    heapq.heappush(heap, skipped)
                else:
                    return res
            else:
                freq, char = heapq.heappop(heap)
                res += char
                freq +=1
                if freq == 0:
                    continue
                heapq.heappush(heap, (freq, char))
        return res


