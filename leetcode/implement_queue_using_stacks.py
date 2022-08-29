class MyQueue:
    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> int:
        stack_2 = []

        while len(self.stack) > 0:
            stack_2.append(self.stack.pop())
        pop = stack_2.pop()
        while len(stack_2) > 0:
            self.stack.append(stack_2.pop())
        return pop

    def peek(self) -> int:
        stack_2 = []
        while len(self.stack) > 0:
            stack_2.append(self.stack.pop())
        peek = stack_2[-1]
        while len(stack_2) > 0:
            self.stack.append(stack_2.pop())
        return peek

    def empty(self) -> bool:
        return len(self.stack) == 0
