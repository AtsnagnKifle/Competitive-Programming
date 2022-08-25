class Solution:
    def nextGreaterElement(self, nums1, nums2):
        dic_map = {}
        stack = []
        nums2_len = len(nums2)
        stack.append(nums2[0])

        for i in range(1, nums2_len):
            if nums2[i] < stack[-1]:
                stack.append(nums2[i])
            else:
                while nums2[i] > stack[-1]:
                    dic_map[stack[-1]] = nums2[i]
                    stack.pop()

                    if len(stack) == 0:
                        break

                stack.append(nums2[i])

        ans = []
        for i in nums1:
            if i in dic_map:
                ans.append(dic_map[i])
            else:
                ans.append(-1)
        return ans
