# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode()
        tail = dummy
        while l1 or l2 or carry != 0:
            print(".")
            if (l1 and l2):
                s = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif not l1 and l2:
                s = l2.val + carry
                l2 = l2.next
            elif not l2 and l1:
                s = l1.val + carry
                l1 = l1.next
            else:
                s = carry
            carry = s // 10
            tail.next = ListNode(s%10, None)
            tail = tail.next
        return dummy.next
    

        

        