class MinStack:

    def __init__(self):
        self.s = []
        self.min = []
                

    def push(self, val: int) -> None:
        self.s.append(val)
        if self.min:
            temp = self.min[-1]
        else:
            temp = val
        val = min(val, temp)
        self.min.append(val)

                

    def pop(self) -> None:
        self.s.pop()
        self.min.pop()



    def top(self) -> int:
        return self.s[-1]
        

    def getMin(self) -> int:
        return self.min[-1]