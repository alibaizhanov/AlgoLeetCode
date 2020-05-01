# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    # recursively
    def preorderTraversal(self, root):
        res = []
        self.dfs(root, res)
        return res

    def dfs(self, root, res):
        if root:
            res.append(root.val)
            self.dfs(root.left, res)
            self.dfs(root.right, res)
    """
    #Iteratively
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        
        if root is None:
            return []
        
        stack = []
        rList= []
        
        stack.append(root)
        
        while len(stack) !=0:
            
            temp = stack.pop()
            rList.append(temp.val)
            
            if temp.right is not None:
                stack.append(temp.right)
            
            if temp.left is not None:
                stack.append(temp.left)
        
        
        return rList
    """
    
        

        