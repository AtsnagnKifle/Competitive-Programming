def smallerNumbersThanCurrent(self, nums):
    ans = []
    length = len(nums)

    for i in range(length):
        co = 0
        for j in range(length):
            if nums[i] > nums[j]:
                co += 1
        ans.append(co)
    return ans
