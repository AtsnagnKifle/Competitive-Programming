class Solution:
    def isValid(self, s: str) -> bool:
        l = []

        for char in s:
            if char == '(' or char == '{' or char == '[':
                l.append(char)
            else:
                if len(l) < 1:
                    return False
                if char == ")":
                    if l[-1] == '(':
                        l.pop()
                    else:
                        return False
                if char == "}":
                    if l[-1] == '{':
                        l.pop()
                    else:
                        return False
                if char == "]":
                    if l[-1] == '[':
                        l.pop()
                    else:
                        return False
        if len(l) == 0:
            return True
        else:
            return False
