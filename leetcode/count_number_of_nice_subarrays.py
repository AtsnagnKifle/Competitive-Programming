class Solution:
    def numberOfSubarrays(self, nums, k):
        n = len(nums)
        count = 0
        prefix = [0] * (n+1)
        odd = 0

        for i in range(n):
            prefix[odd] += 1
            if (nums[i] % 2 == 1):
                odd += 1
            if (odd >= k):
                count += prefix[odd - k]

        return count
