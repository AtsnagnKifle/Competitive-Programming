# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head):
        li = []
        n = 1
        ans = 0
        while head.next:
            n += 1
            li.append(head.val)
            head = head.next
        li.append(head.val)
        for i in range(n//2):
            ans = max(ans, li[i]+li[n-1-i])

        return ans
