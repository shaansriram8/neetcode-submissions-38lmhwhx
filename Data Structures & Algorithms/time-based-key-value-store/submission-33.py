class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ""
        search_space = self.store[key] 
        if len(search_space) == 0:
            return ""
        #gives us a list of shape: [(timestamp, value), ...]
        #alice: (1, happy), (3, sad)
        l, r = 0, len(search_space) - 1
        while l <= r:
            mid = (l + r) // 2
            if search_space[mid][0] == timestamp:
                return search_space[mid][1]
            elif search_space[mid][0] < timestamp:
                l = mid + 1
            else:
                r = mid - 1
        return search_space[r][1] if r >= 0 else ""
                




        

        
