class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for tok in tokens:
            if tok == "+":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1) + int(num2))

            elif tok == "-":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1) - int(num2))

            elif tok == "*":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1) * int(num2))

            elif tok == "/":
                num2 = stack.pop()
                num1 = stack.pop()
                stack.append(int(num1) / int(num2))
            else:
                stack.append(tok)
        return int(stack[0])