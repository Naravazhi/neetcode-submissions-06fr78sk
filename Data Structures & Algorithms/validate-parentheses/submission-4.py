class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map_brackets = {"(" : ")", "[" : "]", "{" : "}"}
        for char in s:
            if char == "(" or char == "[" or char == "{":
                stack.append(char)
            elif char == ")" or char == "]" or char == "}":
                if stack:
                    popped = stack.pop()
                    if char != map_brackets[popped]:
                        return False
                else:
                    return False
        return True if len(stack) == 0 else False