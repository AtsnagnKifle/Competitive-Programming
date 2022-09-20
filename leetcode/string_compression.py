class Solution:
    def compress(self, chars):
        s = ""
        chars_len = len(chars)
        i = 0
        while i < chars_len:
            char = chars[i]
            j = i+1
            co = 1
            while j < chars_len:
                if chars[j] == char:
                    co += 1
                else:
                    break
                j += 1
            if co == 1:
                s += str(char)
            else:
                s += str(char)+str(co)
            i = j
        chars[0:0] = list(s)
        return len(s)
