class MinStack:

    def __init__(self):
        self.l=[]
        self.l1=[]
        

    def push(self, val: int) -> None:
        if len(self.l)!=0:
            if val <= self.l1[-1]:
                self.l1.append(val)
        else:
            self.l1.append(val)
        self.l.append(val)


    def pop(self) -> None:
        if self.l[-1] == self.l1[-1]:
            self.l1.pop()
        self.l.pop()

    def top(self) -> int:
        return self.l[-1]

    def getMin(self) -> int:
        return self.l1[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
