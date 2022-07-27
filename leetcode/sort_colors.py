class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        ans = [0, 0, 0]
        for num in nums:
            ans[num] += 1
        n = []
        for i in range(3):
            n = n + (ans[i]*[i])
        for i in range(len(nums)):
            nums[i] = n[i]
