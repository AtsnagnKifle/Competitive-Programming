# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head):
        new_head = ListNode(0, head)
        i = new_head
        j = head

        while j:

            if j.next and j.val == j.next.val:
                while j.next and j.val == j.next.val:
                    j = j.next
                i.next = j.next
            else:
                i = i.next

            j = j.next

        return new_head.next
