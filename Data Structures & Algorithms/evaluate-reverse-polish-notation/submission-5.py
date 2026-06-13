import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = {"+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": lambda a, b: int(a/b)
        }
        for tok in tokens:
            if tok in op:
                y = stack.pop()
                x = stack.pop()
                stack.append(op[tok](x, y))
            else: 
                stack.append(int(tok))
        return stack[-1]
        