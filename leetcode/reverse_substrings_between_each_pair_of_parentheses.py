class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for char in s:
            if char is ")":
                string = ""
                while not stack[-1] == "(":
                    string += stack.pop()
                stack.pop()
                for c in string:
                    stack.append(c)
            else:
                stack.append(char)
        return "".join(stack)
