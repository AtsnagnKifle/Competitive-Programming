class Solution:
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        last = 0
        nums_len = len(nums)
        for i in range(nums_len):
            if nums[i] != 0:
                nums[last] = nums[i]
                last += 1
        for i in range(last, nums_len):
            nums[i] = 0
