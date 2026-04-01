import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       
     hashmap = {}
     heapx = []
     output = []

     for num in nums:
        hashmap[num] = hashmap.get(num, 0) + 1

     for key, val in hashmap.items():
        pair = (-val, key) #key is number, val is frequency
        heapq.heappush(heapx, pair)
    
     for i in range(k):
        pair = heapq.heappop(heapx)
        output.append(pair[1])
     return output



        

        

            