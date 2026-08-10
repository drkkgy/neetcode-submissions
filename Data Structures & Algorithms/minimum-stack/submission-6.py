class MinStack:

    def __init__(self):
        self.mem = []
        self.min = None
        self.aux = []
        
    def push(self, val: int) -> None:
        
        self.mem.append(val)
        if self.min is None:
            self.min = val
        else:
            self.min = min(self.min,val)
        self.aux.append(self.min)
        

    def pop(self) -> None:
        self.mem.pop(-1)
        self.aux.pop(-1)

        # Restore the minimum for the new top of the stack
        self.min = self.aux[-1] if self.aux else None

    def top(self) -> int:
        return self.mem[-1]
        

    def getMin(self) -> int:
        return self.aux[-1]
        
