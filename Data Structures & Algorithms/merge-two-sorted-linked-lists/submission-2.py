# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head, tail = None, None
        while list1 is not None or list2 is not None:
            if (list2 is None) or (list1 is not None and list1.val < list2.val):
                if head is None:
                    head, tail = list1, list1
                else:
                    tail.next = list1
                    tail = tail.next
                list1 = list1.next
            elif (list1 is None) or (list2 is not None and list2.val <= list1.val):
                if head is None:
                    head, tail = list2, list2
                else:
                    tail.next = list2
                    tail = tail.next
                list2 = list2.next
        if tail is not None:
            tail.next = None
        return head
        





        