from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        a = deque([p]) if p else deque()
        b = deque([q]) if q else deque()

        while a:
            if b:
                node1 = a.pop()
                node2 = b.pop()
                if node1.val == node2.val:
                    if node1.left is None and node2.left is None:
                        pass
                    elif node1.left and node2.left:
                        a.append(node1.left)
                        b.append(node2.left)
                    else:
                        return False

                    if node1.right is None and node2.right is None:
                        pass
                    elif node1.right and node2.right:
                        a.append(node1.right)
                        b.append(node2.right)
                    else:
                        return False 
                else:
                    return False
            else:
                return False

        if not a and not b:
            return True
        return False    

     



        