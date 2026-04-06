class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                # if stack[-1] and stack[-2]:
                if len(stack) >= 2:
                    stack.append(stack.pop() + stack.pop())

            elif token == "-":
                # if stack[-1] and stack[-2]:
                if len(stack) >= 2:
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(first - second)
            
            elif token == "*":
                # if stack[-1] and stack[-2]:
                if len(stack) >= 2:
                    stack.append(stack.pop() * stack.pop())

            elif token == "/":
                # if stack[-1] and stack[-2]:
                if len(stack) >= 2:
                    second = stack.pop()
                    first = stack.pop()
                    stack.append(int(first / second))
            else:
                # just a number so add to stack
                stack.append(int(token)) # cast to int

        return stack[0]