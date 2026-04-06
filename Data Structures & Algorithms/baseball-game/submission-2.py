class Solution:
    def calPoints(self, operations: List[str]) -> int:


        stack = []

        for op in operations:
            if op == "+":
                if stack[-1] and stack[-2]:
                    stack.append(stack[-1] + stack[-2])
            elif op == "D":
                if stack[-1]:
                    num = stack[-1]
                    stack.append(num * 2)
            elif op == "C":
                if stack[-1]:
                    stack.pop()
            else:
                stack.append(int(op))

        return sum(stack)





































        
        # stack = []

        # for op in operations:
        #     if op == "+":
        #         num2 = int(stack[-1])
        #         num1 = int(stack[-2])
        #         stack.append(num1 + num2)

        #     elif op == "D":
        #         num2 = int(stack[-1])
        #         stack.append(2 * num2)

        #     elif op == "C":
        #         stack.pop()
        #     else:
        #         stack.append(op)

        # curSum = 0
        # for char in stack:
        #     curSum += int(char)

        # return curSum



