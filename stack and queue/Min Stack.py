# https://leetcode.com/problems/min-stack/
class MinStack:
    def __init__(self):
        self.stack = []
        self.monostack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.monostack:
            self.monostack.append(min(val, self.monostack[-1]))
        else:
            self.monostack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.monostack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.monostack[-1]


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
curmin = obj.getMin()
obj.pop()
obj.top()
curmin = obj.getMin()
