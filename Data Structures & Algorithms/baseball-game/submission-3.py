class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for operation in operations:
            if operation == "+":
                if len(stack) >= 2:
                    ans = stack[-1] + stack[-2]
                    stack.append(ans)
            elif operation == "D":
                if stack:
                    double = 2 * stack[-1]
                    stack.append(double)
            elif operation == "C":
                if stack:
                    stack.pop()

            else:
                stack.append(int(operation))
        

        return sum(stack)

