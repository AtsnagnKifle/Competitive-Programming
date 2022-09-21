class Solution:
    def lengthOfLongestSubstring(self, s):
        s_len = len(s)
        left = 0
        right = 0
        dic = {}
        ans = 0
        while right < s_len:
            r_char = s[right]
            if r_char in dic:
                dic[r_char] += 1
            else:
                dic[r_char] = 1

            while(dic[r_char] > 1):
                l_char = s[left]
                dic[l_char] -= 1
                left += 1
            ans = max(ans, right+1-left)
            right += 1

        return ans
