class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for num in asteroids:
            if not stack: #empty stack
                stack.append(num)
            elif stack[-1] > 0 and num < 0:
                top, new = stack[-1], abs(num)
                if top == new:
                    stack.pop() #top and new lose
                    continue
                elif top > new:
                    continue #top wins, dont append new
                elif top < new: 
                    #while nums in stack and while
                    #top of stack is positive and while
                    #top of stack < new
                    while stack and stack[-1] > 0 and stack[-1] < new:
                        stack.pop()
                    if not stack or stack[-1] < 0:
                        stack.append(num)
                    elif stack[-1] == new:
                        stack.pop()
            else: #same direction
                stack.append(num)

                
        return stack