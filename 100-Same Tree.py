Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        
        if p is None and q is None:
            
            return True
        
        if p is not None and q is not None:
            
            a = True if p.val == q.val else False
        
            b = self.isSameTree(p.left,q.left)
        
            c = self.isSameTree(p.right,q.right)
            
            if a and b and c:
                
                return True
            
        return False
        
        
        