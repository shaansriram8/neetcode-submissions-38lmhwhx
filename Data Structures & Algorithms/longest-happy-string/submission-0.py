class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        queue = deque()
        out = ""

        vals = [a, b, c]
        for ind, val in enumerate(vals):
            if val > 0:
                heapq.heappush(heap, (-val, chr(ord('a') + ind)))


        while heap:
            if len(out) < 2:
                freq, letter = heapq.heappop(heap)
                out += letter
                freq +=1
                #if freq < 0:
                    #heapq.heappush(heap, (freq, letter))
            else:
                if out[-1] == out[-2] == heap[0][1]:
                    if len(heap) == 1:
                        break
                    blocked = heapq.heappop(heap)
                    #next available:
                    freq, letter = heapq.heappop(heap)
                    out += letter
                    freq +=1
                    heapq.heappush(heap, blocked)
                else:
                    freq, letter = heapq.heappop(heap)
                    out += letter
                    freq +=1

            if freq < 0:
                heapq.heappush(heap, (freq, letter))
        return out


        