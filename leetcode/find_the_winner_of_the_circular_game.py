class Solution:
    def longestSubarray(self, nums, limit):
        while len(nums) > 1:
            for i in range(limit-1):
                no = nums.pop(0)
                nums.append(no)
            nums.pop(0)
        print(nums)
