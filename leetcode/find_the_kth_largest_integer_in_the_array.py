class Solution:
    def kthLargestNumber(self, nums, k):
        nums.sort(key=lambda x: int(x))
        return nums[-k]
