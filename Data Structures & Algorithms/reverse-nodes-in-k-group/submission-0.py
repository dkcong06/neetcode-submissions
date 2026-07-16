# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        start = None
        groupTail = None
        while head is not None:
            nodes = [None] * k
            for i in range(k):
                if head is None:
                    break
                nodes[i] = head
                head = head.next
            if nodes[-1] is not None:
                if start is None:
                    start = nodes[-1]
                for i in range(k-1):
                    nodes[i+1].next = nodes[i]
                if groupTail is not None:
                    groupTail.next = nodes[k-1]
                groupTail = nodes[0]
            else:
                if groupTail:
                    groupTail.next = nodes[0]
                    return start
        groupTail.next = None
        return start
            


            

        