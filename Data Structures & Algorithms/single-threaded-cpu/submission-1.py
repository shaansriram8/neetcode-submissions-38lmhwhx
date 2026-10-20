class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #tasks[i] = [enqueueTime, processingTime]
        heap = []
        #[1, 4] [2, 1] [3, 3]
        sorted_tasks = sorted((enq, proc, i) for i, (enq, proc) in enumerate(tasks))
        res = []
        t = sorted_tasks[0][0]
        i = 0
        while heap or i < len(tasks):
            while i < len(tasks) and sorted_tasks[i][0] <= t:
                #sort by processing time, then index
                heapq.heappush(heap, (sorted_tasks[i][1], sorted_tasks[i][2]))
                i+=1
            if not heap:
                t = sorted_tasks[i][0]
            else:
                value = heapq.heappop(heap) #processingTime, index
                t += value[0]
                res.append(value[1])
        return res



        





