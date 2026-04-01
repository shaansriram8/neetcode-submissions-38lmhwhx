class FirstUnique:

    def __init__(self, nums: List[int]):
        self.nums = nums #persistent nums
        self.seen = {} #frequency maping
        for num in self.nums:
            self.seen[num] = self.seen.get(num, 0) + 1 #initial freq mapping

    def showFirstUnique(self) -> int:
        for num in self.seen:
            if self.seen[num] == 1: #return first unique number
                return num
        return -1

    def add(self, value: int) -> None:
        self.nums.append(value) #append new value
        if value in self.seen:
            self.seen[value] +=1 
        else:
            self.seen[value] = 1

# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)
