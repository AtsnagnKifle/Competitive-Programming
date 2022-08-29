class Solution:
    def fib(self, n: int) -> int:
        return self.findfib(n)

    def findfib(self, n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        return self.findfib(n-1)+self.findfib(n-2)
