class MinStack:

    def __init__(self):
        self.stack = []
        self.minstack = []
        self.mini = None

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.mini == None or val < self.mini:
            self.mini = val
        self.minstack.append(self.mini)
        return None

    def pop(self) -> None:
        self.stack.pop()
        self.minstack.pop()
        if len(self.minstack) != 0:
            self.mini = self.minstack[-1]
        else:
            self.mini = None
        return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minstack[-1]
            
        
