class MyStack:

    def __init__(self):

        self.mem = []
        

    def push(self, x: int) -> None:

        self.mem.append(x)
        

    def pop(self) -> int:
        val = self.mem[-1]
        self.mem.pop(-1)
        return val
        

    def top(self) -> int:
        return self.mem[-1]
        

    def empty(self) -> bool:
        return False if self.mem else True
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()