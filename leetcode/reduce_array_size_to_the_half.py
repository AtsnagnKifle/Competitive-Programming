class Solution:
    def minSetSize(self, arr):
        arr_len = len(arr)
        dic = {}
        ans = 0
        red_arr = 0
        for i in arr:
            if i in dic.keys():
                dic[i] += 1
            else:
                dic[i] = 1
        val = sorted(list(dic.values()), reverse=True)
        for i in val:
            if red_arr >= (arr_len/2):
                break
            else:
                ans += 1
                red_arr += i
        return ans
