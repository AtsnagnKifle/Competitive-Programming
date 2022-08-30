class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        ans = self.find(n)
        return ans[k-1]

    def find(self, n):
        if n <= 1:
            return "0"
        st = self.find(n-1)
        return st + "1"+self.reverse(self.invert(st))

    def reverse(self, string):
        return string[::-1]

    def invert(self, string):
        st = ["0" if i == "1" else "1" for i in string]
        return "".join(st)
