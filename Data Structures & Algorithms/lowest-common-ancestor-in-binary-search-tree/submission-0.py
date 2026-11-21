# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        tree = deque([root])
        while tree:
            node = tree.popleft()
            if p.val > node.val and q.val > node.val:
                tree.append(node.right)
            elif p.val < node.val and q.val < node.val:
                tree.append(node.left)
            else:
                return node
            
        