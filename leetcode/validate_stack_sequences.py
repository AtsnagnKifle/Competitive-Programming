class Solution:
    def validateStackSequences(self, pushed, popped):
        stack = []
        for i in pushed:
            stack.append(i)
            while len(stack) > 0 and stack[-1] == popped[0]:
                stack.pop()
                del popped[0]

        return stack == []
