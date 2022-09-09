# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1, list2):
        node = ListNode()
        ans = node
        while list1 and list2:
            if list1.val >= list2.val:
                node.next = ListNode(list2.val)
                list2 = list2.next
            else:
                node.next = ListNode(list1.val)
                list1 = list1.next
            node = node.next
        self.mergeTheRem(node, list1)
        self.mergeTheRem(node, list2)

        return ans.next

    def mergeTheRem(self, node, lst):
        while lst:
            node.next = ListNode(lst.val)
            lst = lst.next
            node = node.next
