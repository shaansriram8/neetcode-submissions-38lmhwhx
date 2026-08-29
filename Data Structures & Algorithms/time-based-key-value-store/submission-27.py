class TimeMap:

    def __init__(self):
        self.hashmap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashmap:
            self.hashmap[key] = []
        self.hashmap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        #if the key does not exist or there is no associated value, early return
        if key not in self.hashmap or len(self.hashmap[key]) == 0:
            return ""
        #at this point, we can ensure that there exists an ordered list of timestamps.
        l, r = 0, len(self.hashmap[key])-1
        #run binary search to find the optimal timestamp. This is defined as
        #largest timestamp_prev s.t. timestamp_prev <= timestamp as the upper bound

        #best_seen is the best seen timestamp
        best_seen = ""
        while l <= r:
            mid = l + (r - l) // 2
            val, t = self.hashmap[key][mid]
            if t > timestamp:
                r = mid - 1
            elif t < timestamp:
                best_seen = val
                l = mid + 1
            else:
                return val
        return best_seen


        


            
            

        
