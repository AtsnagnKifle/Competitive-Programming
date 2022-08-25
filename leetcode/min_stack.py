class MinStack:

    def __init__(self):
        self.stack = []
        self.stack_min = []
        self.stack_min_counter = 0

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.stack_min_counter:
            self.stack_min.append(val)
            self.stack_min_counter += 1
        else:
            if self.stack_min[-1] >= val:
                self.stack_min.append(val)
                self.stack_min_counter += 1

    def pop(self) -> None:
        item = self.stack.pop()
        if self.stack_min[-1] == item:
            self.stack_min.pop()
            self.stack_min_counter -= 1

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.stack_min[-1]
