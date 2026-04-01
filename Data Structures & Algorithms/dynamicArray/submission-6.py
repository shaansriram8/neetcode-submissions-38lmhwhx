class DynamicArray:
    
    def __init__(self, capacity: int):
        if capacity < 0:
            raise ValueError("Capacity must be non-negative")
        self.capacity = capacity
        self.arr = [None] * capacity
        self.size = 0


    def get(self, i: int) -> int:
        if 0 <= i < self.capacity:
            return self.arr[i]
        else:
            raise ValueError("index out of range")

    def set(self, i: int, n: int) -> None:
        if 0 <= i < self.capacity:
            self.arr[i] = n
        else:
            raise ValueError("index out of range")

    def pushback(self, n: int) -> None:
        if self.size == self.capacity:
            self.resize()         
        self.arr[self.size] = n
        self.size += 1

    def popback(self) -> int:
        val = self.arr[self.size-1]
        self.arr[self.size-1] = None
        self.size -= 1
        return val

    def resize(self) -> None:
        newArr = [None] * (self.capacity * 2)
        for i in range(self.size):
            newArr[i] = self.arr[i]
        self.arr = newArr
        self.capacity = self.capacity*2

    def getSize(self) -> int:
        return self.size
    
    def getCapacity(self) -> int:
        return self.capacity
