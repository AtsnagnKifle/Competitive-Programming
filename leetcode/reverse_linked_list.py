# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        prev, cu = None, head

        while cu:
            tmp = cu.next
            cu.next = prev
            prev = cu
            cu = tmp

        return prev
