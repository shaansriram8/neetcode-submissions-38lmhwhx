class MovingAverage:

    def __init__(self, size: int):
        self.window = deque()
        self.size = size

    def next(self, val: int) -> float:
        if len(self.window) < self.size:
            self.window.append(val)
        else:
            self.window.popleft()
            self.window.append(val)
        running = 0
        for num in self.window:
            running += num
        if len(self.window) < self.size:
            return running / len(self.window)
        else:
            print(self.size)
            print(running)
            return running / self.size




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
