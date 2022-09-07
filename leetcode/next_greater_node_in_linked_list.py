# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head):
        stack = []
        ans = []
        ind = 0
        while head.next:
            ans.append(0)
            while len(stack):
                if head.val > stack[-1][0]:
                    ans[stack[-1][1]] = head.val
                    stack.pop()
                else:
                    break
            stack.append([head.val, ind])
            ind += 1
            head = head.next
        while len(stack):
            if head.val > stack[-1][0]:
                ans[stack[-1][1]] = head.val
                stack.pop()
            else:
                break
        ans.append(0)
        return ans
