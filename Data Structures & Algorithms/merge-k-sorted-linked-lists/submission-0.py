# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode(0, None)
        tail = dummy    
        while True:
            temp = None    
            for i in range(len(lists)):
                if lists[i] is None or (temp is not None and lists[i].val > lists[temp].val):
                    continue 
                else:
                    temp = i
            if temp is None:
                break
            print(temp)
            tail.next = lists[temp]
            tail = tail.next
            lists[temp] = lists[temp].next
        return dummy.next

        





































