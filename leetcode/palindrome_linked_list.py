# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head):
        co = 0
        head_copy = head
        vals = []
        while head_copy.next:
            vals.append(head_copy.val)
            head_copy = head_copy.next
        vals.append(head_copy.val)

        return vals == vals[::-1]
