class Solution:
    def myPow(self, x: float, n: int) -> float:
        return self.cal(x, n)

    def cal(self, x, n):
        if n == 0:
            return 1
        if n < 0:
            return 1/self.cal(x, n*-1)

        u = self.cal(x, n//2)
        u = u * u
        if (n % 2 == 1):
            u = u * x
        return u
