# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    #Iteratively
    
    def isSymmetric(self, root):
        
        if not root:
            return True
        
        q = [(root.left,root.right)]
        
        
        while len(q) !=0:
            
            node1,node2 = q.pop(0)
            
            if not node1 and not node2:
                continue
            if not node1 or not node2:
                return False
            if node1.val != node2.val:
                return False
            
            q.append((node1.left,node2.right))
            q.append((node1.right,node2.left))
        
        return True
            
            
    
    
    """
    #Recursively
    def isSymmetric(self, root):
        return self.dfs(root,root)
    def dfs(self,root1,root2):
        if not root1 and not root2:
            return True
        if not root1 or not root2:
            return False
        if root1.val != root2.val:
            return False
        left_side = self.dfs(root1.left, root2.right)
        right_side = self.dfs(root1.right, root2.left)
        return left_side and right_side
    """
            
        