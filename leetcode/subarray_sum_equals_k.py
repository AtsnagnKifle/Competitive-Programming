class Solution:
    def subarraySum(self, nums, k):
        dic = {0: 1}
        ans = 0
        pre_sum = 0

        for i in nums:
            pre_sum += i
            no = pre_sum - k
            if no in dic:
                ans += dic[no]
            if pre_sum in dic:
                dic[pre_sum] += 1
            else:
                dic[pre_sum] = 1

        return ans
