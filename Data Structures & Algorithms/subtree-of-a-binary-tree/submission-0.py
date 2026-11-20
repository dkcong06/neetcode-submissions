# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        tree = deque([root])
        while tree:
            for _ in range(len(tree)):
                node = tree.popleft()
                if node is not None and node.val == subRoot.val:
                    if self.isIdentical(node, subRoot):
                        return True
                if node is not None:
                    tree.append(node.left)
                    tree.append(node.right)
        return False 

    def isIdentical(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        p, q = deque([root1]), deque([root2])
        while p:
            if q:
                node1 = p.popleft()
                node2 = q.popleft()
                if node1 is None and node2 is None:
                    pass
                elif node1 is None or node2 is None:
                    return False
                elif node1.val == node2.val:
                    p.append(node1.left)
                    p.append(node1.right)
                    q.append(node2.left)
                    q.append(node2.right)
                else:
                    return False
            else:
                return False
        if not p and not q:
            return True
        return False

    