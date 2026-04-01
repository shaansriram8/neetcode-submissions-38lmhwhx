class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #the idea is that more days while still under days
        #corresponds to lower minimum weight
        best = 0
        low, high = max(weights), sum(weights) #low = weight if we shipepd one elem
        while low <= high:
            mid = (low + high) // 2
            #12
            dayctr = 1
            curr_load = 0
            for weight in weights:
                if curr_load + weight > mid:
                    dayctr += 1
                    curr_load = 0
                curr_load += weight
            print("mid:", mid)
            print("ctr:", dayctr)
            if dayctr > days:
                low = mid + 1      # too few capacity, go higher
            else:
                best = mid         # feasible, record and try lower
                high = mid - 1
        return best

        #[1, 2, 3]

        [1,5,4,4,2,3]
        #low, high = 0, 5
        #mid = 2
        #2 - 1   days = 1
        #2 - 5   

        #low, high = 10-19
        #mid = 14
        #




         
