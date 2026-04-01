class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = [] #going to contain tuple (temperature, index)
        res = [0] * len(temperatures)

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]: # is stack non empty and is temp greater than temp at top of stack
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd)
            stack.append([t, i])
        return res