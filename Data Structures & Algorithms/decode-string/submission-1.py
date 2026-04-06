class Solution:
    def decodeString(self, s: str) -> str:
        
        stack = []
        output = ""


        for c in s:
            if c == "]":
                sub = ""
                while stack[-1] != "[":
                    sub = stack[-1] + sub
                    stack.pop()
                if stack[-1] == "[":
                    stack.pop()
                    full_sub = ""
                    num = ""
                    while stack and stack[-1].isdigit():
                        num = stack[-1] + num
                        stack.pop()
                    num = int(num)
                    for i in range(num):
                        full_sub += sub
                    for c in full_sub:
                        stack.append(c)
            else:
                stack.append(c)

        while stack:
            output = stack[-1] + output
            stack.pop()
        return output
