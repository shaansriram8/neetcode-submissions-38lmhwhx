class MovingAverage:

    def __init__(self, size: int):
        self.window = deque()
        self.size = size
        self.running = 0

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            self.window.append(val)
            self.running += val
        else:
            x = self.window.popleft()
            self.window.append(val)
            self.running -= x
            self.running += val
            
        return self.running / len(self.window)




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
