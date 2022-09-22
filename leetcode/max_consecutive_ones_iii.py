class Solution:
    def longestOnes(self, nums, k):
        i = 0
        j = 0
        co_0 = 0
        co_1 = 0
        ans = 0
        nums_len = len(nums)

        while i < nums_len:
            if nums[i] == 0:
                co_0 += 1
            if nums[i] == 1:
                co_1 += 1
            while co_0 > k:
                if nums[j] == 0:
                    co_0 -= 1
                j += 1
            ans = max(ans, i+1-j)
            i += 1

        return ans
