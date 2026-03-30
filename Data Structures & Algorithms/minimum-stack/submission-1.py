class MinStack:

    def __init__(self):
        self.stk = []
        self.tp = -69420
        return None

    def push(self, val: int) -> None:
        self.stk.insert(0, val)
        self.tp = val
        return None

    def pop(self) -> None:
        ele = self.stk.pop(0)
        return ele

    def top(self) -> int:
        return self.stk[0]

    def getMin(self) -> int:
        return min(self.stk)
