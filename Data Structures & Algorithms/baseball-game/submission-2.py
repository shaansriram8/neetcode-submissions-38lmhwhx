class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        score = 0

        for i, op in enumerate(operations):
            try:
                x = int(op)
                score += x
                stack.append(x)
            except:
                if stack and op == '+':
                    if len(stack) >= 2:
                        score += (stack[-1] + stack[-2])
                        stack.append((stack[-1] + stack[-2]))
                elif stack and op == 'D':
                    score += stack[-1]*2
                    stack.append(stack[-1]*2)
                elif stack and op == 'C':
                    score -= stack[-1]
                    stack.pop()
        return score


        