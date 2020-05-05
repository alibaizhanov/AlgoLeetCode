# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def sumNumbers(self, root: TreeNode):
        
        if root is None:
            return 0
        
        #Iteratively BFS
        
        res,queue = 0,[(root,root.val)]
        
        while queue:
            
            node,value = queue.pop(0)
            
            if not node.left and not node.right:
                res  = res + value
            
            if node.left:
                queue.append((node.left,value*10 + node.left.val))
            
            if node.right:
                queue.append((node.right,value*10 + node.right.val))
        
        return res
        
        
        
    
    """
    #Recursively DFS
    def sumNumbers(self, root: TreeNode) -> int:
        
        if root is None:
            return 0
        
        res = []
        self.dfsSum(root,res,0)
        
        return sum(res)
        
    
    def dfsSum(self,root,res,val):
        
        if root is None:
            return
        
        val = val * 10 + root.val
        
        self.dfsSum(root.left,res,val)
        self.dfsSum(root.right,res,val)
        
        if not root.left and not root.right:
            res.append(val)
    """