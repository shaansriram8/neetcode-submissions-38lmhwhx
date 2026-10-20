class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        rows, res, heap = [], [], []
        for i, (enq, proc) in enumerate(tasks):
            rows.append((enq, proc, i))
        sorted_tasks = sorted(rows)
        i, t = 0, sorted_tasks[0][0]
        while heap or i < len(tasks):
            while i < len(tasks) and sorted_tasks[i][0] <= t:
                #push the processing time and index of the task
                heapq.heappush(heap, (sorted_tasks[i][1], sorted_tasks[i][2]))
                i+=1
            if not heap:
                t = sorted_tasks[i][0]
            else:
                val = heapq.heappop(heap)
                processingT = val[0]
                t += processingT
                index = val[1]
                res.append(index)

        return res
