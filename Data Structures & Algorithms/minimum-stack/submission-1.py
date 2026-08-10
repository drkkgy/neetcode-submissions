class MinStack:

    def __init__(self):
        self.mem = []
        
    def push(self, val: int) -> None:
        self.mem.append(val)

    def pop(self) -> None:
        self.mem.pop(-1)

    def top(self) -> int:
        return self.mem[-1]
        

    def getMin(self) -> int:
        return min(self.mem)
        
