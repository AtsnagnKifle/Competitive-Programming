class Solution:
    def maxArea(self, height):
        i = 0
        j = len(height)-1
        ans = 0
        while not i == j:
            ans = max(ans, min(height[i], height[j])*(j-i))
            if height[i] > height[j]:
                j -= 1
            else:
                i += 1
        return ans
