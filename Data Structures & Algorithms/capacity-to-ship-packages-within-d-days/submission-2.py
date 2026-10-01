class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)

    
        i = 0
        day_total = 0

        while low < high:
            mid = (low + high) // 2
            day = 0
            i = 0
            while day < days:
                day_total = 0
                while i < len(weights) and day_total < mid:
                    if day_total + weights[i] > mid:
                        break
                    day_total += weights[i]
                    i+=1
                day +=1
            if i == len(weights):  
                high = mid           
            else:
                low = mid + 1 
        return low
            

            
            
            


        