class Solution:
    def getDescentPeriods(self, prices):
        prices_len = len(prices)
        ans = 1
        co = 1
        for i in range(1, prices_len):
            if (prices[i-1]-1) == prices[i]:
                co += 1
            else:
                co = 1
            ans += co
        return ans
