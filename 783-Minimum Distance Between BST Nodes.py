# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        
        res = []
        
        def appEnd(root):
            
            if root is None:
                return
            
            res.append(root.val)
            
            appEnd(root.left)
            appEnd(root.right)
        
        appEnd(root)
        sRes = sorted(res)
        diff = []
        for i in range(len(sRes)-1):
            
            diff.append(sRes[i+1] - sRes[i])
            
        return min(diff)
            
            
        