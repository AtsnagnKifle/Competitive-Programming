# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head):
        linked_list_len = 1
        head_copy = head
        while not head_copy.next == None:
            linked_list_len += 1
            head_copy = head_copy.next
        mid = linked_list_len//2
        for _ in range(mid):
            head = head.next

        return head
