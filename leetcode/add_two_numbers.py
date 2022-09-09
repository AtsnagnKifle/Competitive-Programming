# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1, l2):
        rem = 0
        new_node = ListNode()
        ans = new_node
        while l1 or l2:
            l1_val = 0
            l2_val = 0
            if l1:
                l1_val = l1.val
            if l2:
                l2_val = l2.val
            n = l1_val + l2_val + rem
            no = n % 10
            rem = n // 10
            new_node.next = ListNode(no)
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            new_node = new_node.next
        n = rem
        while n:
            no = n % 10
            new_node.next = ListNode(no)
            n = n//10

        return ans.next
