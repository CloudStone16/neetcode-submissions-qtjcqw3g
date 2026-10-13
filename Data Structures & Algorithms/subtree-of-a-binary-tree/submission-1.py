# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False

        if root.val == subRoot.val:
            if self.equality(root, subRoot):
                return True
        
        f1 = self.isSubtree(root.left, subRoot)
        f2 = self.isSubtree(root.right, subRoot)
        return f1 | f2
            

    def equality(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        
        f1 = self.equality(p.left, q.left)
        f2 = self.equality(p.right, q.right)
        return f1 & f2