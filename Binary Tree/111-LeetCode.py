# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        
    def maxDepth(self,root):
        
        queue = [(root,1)]
        maxDepth = 0
        
        while queue:
            
            node,level = queue.pop(0)
            
            if node.left is None and node.right is None:
                return level
            
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
        
        
    
    
    def minDepth(self,root):
        queue = [(root,1)]
        
        while queue:
            
            node,level = queue.pop(0)
            
            if node.left is None and node.right is None:
                return level
            
            if node.left:
                queue.append((node.left,level+1))
            if node.right:
                queue.append((node.right,level+1))
            
        