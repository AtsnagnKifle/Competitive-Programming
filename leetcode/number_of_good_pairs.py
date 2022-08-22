class Solution:
    def numIdenticalPairs(self, nums) -> int:
        ans = 0
        nums_len = len(nums)
        for i in range(nums_len-1):
            for j in range(i+1, nums_len):
                if nums[i] == nums[j]:
                    ans += 1
        return ans
