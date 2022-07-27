class Solution:
    def targetIndices(self, nums, target):
        ans = []
        length = len(nums)
        for i in range(length-1):
            for j in range(i+1, length):
                if nums[i] > nums[j]:
                    temp = nums[i]
                    nums[i] = nums[j]
                    nums[j] = temp
        for i in range(length):
            if nums[i] > target:
                break
            elif nums[i] == target:
                ans.append(i)

        return ans
