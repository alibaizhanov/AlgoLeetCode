# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        
        res,stack = [],[(root,"")]
        
        while stack:
            
            node,ls = stack.pop()
            if not node.right and not node.left:
                res.append(ls + str(node.val))
            
            ls = ls + str(node.val) + "->"
            
            if node.right:
                stack.append((node.right,ls))
            
            if node.left:
                stack.append((node.left,ls))
        
        return res
        
    """
    #Recursively
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        if not root:
            return []
        res = []
        self.dfs(root,"",res)
        return res
        
    def dfs(self, root, ls, res):
        if not root.left and not root.right:
            res.append(ls+str(root.val))
            return
            
        ls = ls + str(root.val) + "->"
        
        if root.left:
            self.dfs(root.left,ls,res)
        if root.right:
            self.dfs(root.right,ls,res)
    """
        