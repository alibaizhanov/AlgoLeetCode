# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parent = {root:None}
        
        stack = []
        stack.append(root)
        
        while q not in parent or p not in parent:
            node = stack.pop()
            
            if node.left is not None:
                stack.append(node.left)
                parent[node.left] = node
                
            if node.right is not None:
                stack.append(node.right)
                parent[node.right] = node
        
        ancestors = set()
        while p:
            ancestors.add(p)
            p = parent[p]
        
        
        while q not in ancestors:
            q = parent[q]
        
        return q
            
            