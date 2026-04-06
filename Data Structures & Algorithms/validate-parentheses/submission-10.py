class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {")":"(", "]":"[", "}":"{"}
        for ch in s:
            if ch in pairs:
                if not stack or stack[-1] != pairs[ch]:
                    return False
                stack.pop()
            elif ch in "{[(":
                stack.append(ch)
            else:
                return False
        return True if len(stack) == 0 else False
        
        # stack = []
        # for i in range(len(s)):
        #     if s[i] == "}":
        #         if stack:
        #             if stack[-1] == "{":
        #                 stack.pop()
        #             else:
        #                 return False
        #         else:
        #             return False
        #     elif s[i] == "]":
        #         if stack:
        #             if stack[-1] == "[":
        #                 stack.pop()
        #             else:
        #                 return False
        #         else:
        #             return False
        #     elif s[i] == ")":
        #         if stack:
        #             if stack[-1] == "(":
        #                 stack.pop()
        #             else:
        #                 return False
        #         else:
        #             return False
        #     else:
        #         stack.append(s[i])

        # return True if len(stack) == 0 else False





















        # stack = []

        # for char in s:
        #     if char == ")":
        #         if stack and stack[-1] == "(":
        #             stack.pop()
        #         else:
        #             return False
        #     elif char == "]":
        #         if stack and stack[-1] == "[":
        #             stack.pop()
        #         else:
        #             return False
        #     elif char == "}":
        #         if stack and stack[-1] == "{":
        #             stack.pop()
        #         else:
        #             return False
                    
        #     else:
        #         stack.append(char)

        # return len(stack) == 0 
