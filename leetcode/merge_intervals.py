class Solution:
    def merge(self, intervals):
        intervals.sort()
        intervals_len = len(intervals)
        ans = []
        for i in range(intervals_len):
            if not (i+1) == intervals_len and intervals[i][1] >= intervals[i+1][0]:
                intervals[i+1] = [intervals[i][0],
                                  max(intervals[i+1][1], intervals[i][1])]
            else:
                ans.append(intervals[i])
        return ans
