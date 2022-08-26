class Solution:
    def dailyTemperatures(self, temperatures):
        temp_len = len(temperatures)
        ans = [0]*temp_len
        stack = [[temperatures[0], 0]]
        day_counter = 0

        for i in range(1, temp_len):
            day_counter += 1
            if temperatures[i] < stack[-1][0]:
                stack.append([temperatures[i], i])
            else:
                while temperatures[i] > stack[-1][0]:
                    poped = stack.pop()
                    ans[poped[1]] = i - poped[1]
                    if len(stack) == 0:
                        break
                stack.append([temperatures[i], i])
        return ans
