class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        total = 0

        for operation in operations:
            try:
                stack.append(int(operation))       # append the converted integer
            except ValueError:
                if operation == 'D':
                    stack.append(stack[-1]*2)
                elif operation == 'C':
                    stack.pop()
                else:
                    combined = stack[-2] + stack[-1]
                    stack.append(combined)
            
        return sum(stack)

