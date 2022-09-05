# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        head_copy = head
        linked_list_len = 1
        while not head_copy.next == None:
            linked_list_len += 1
            head_copy = head_copy.next
        nth = linked_list_len - n
        if linked_list_len == 1:
            return None
        if not nth:
            return head.next
        head_copy = head
        for _ in range(nth-1):
            head_copy = head_copy.next
        head_copy.next = head_copy.next.next

        return head
