class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for ind, token in enumerate(tokens):
            try:
                stack.append(int(token))
            except ValueError:
                
                b = stack.pop()
                a = stack.pop()
                if token == '+':
                    stack.append(a+b)
                elif token == '-':
                    stack.append(a-b)
                elif token == '*':
                    stack.append(a*b)
                elif token == '/':
                    stack.append(int(a/b))
        return stack[-1]
        