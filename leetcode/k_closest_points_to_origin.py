class Solution:
    def kClosest(self, points, k):
        li = []
        ans = []
        for point in points:
            dis = point[0]**2+point[1]**2
            li.append([dis, point])
        li.sort()
        for i in range(k):
            ans.append(li[i][1])
        return ans
