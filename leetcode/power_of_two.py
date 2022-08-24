import math


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        x = math.log10(n)/math.log10(2)
        return x == int(x)
