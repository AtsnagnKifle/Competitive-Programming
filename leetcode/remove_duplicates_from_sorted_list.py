# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head):
        first = head
        second = head
        if not head or not head.next:
            return head
        while first.next:
            while (second) and (second.val == first.val):
                second = second.next
            first.next = second
            if not first.next:
                break
            first = first.next

        return head
