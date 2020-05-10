# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    #Iteratively
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        if root is None:
            return []
        
        q = collections.deque()
        res = []
        ls=[]
        q.append((root,sum-root.val,ls + [root.val]))
        
        while q:
            node,val,l = q.popleft()
            
            if not node.left and not node.right and val ==0:
                res.append(l)
            
            if node.left:
                q.append((node.left,val-node.left.val,l + [node.left.val]))
            
            if node.right:
                q.append((node.right,val-node.right.val,l + [node.right.val]))
        
        return res
                
        
        
        
    
    """
    #Recursively
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        
        if root is None:
            return []
        
        res = []
        self.dfs(root,res,[],sum)
        
        return res
        
    def dfs(self,root,res,t,sum):
        
        if not root.left and not root.right:
            if sum == root.val:
                t.append(root.val)
                res.append(t)
        if root.left:
            self.dfs(root.left,res,t + [root.val],sum-root.val)
        if root.right:
            self.dfs(root.right,res,t + [root.val],sum-root.val)
    """