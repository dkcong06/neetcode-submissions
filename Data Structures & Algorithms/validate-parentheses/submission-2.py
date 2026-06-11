class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char == "(":
                stack.append(1)
            if char == "{":
                stack.append(2)
            if char == "[":
                stack.append(3)
            if char == ")":
                if len(stack) == 0 or stack.pop() != 1:
                    return False
            if char == "}":
                if len(stack) == 0 or stack.pop() != 2:
                    return False
            if char == "]":
                if len(stack) == 0 or stack.pop() != 3:
                    return False
        if len(stack) != 0:
            return False
        return True

        