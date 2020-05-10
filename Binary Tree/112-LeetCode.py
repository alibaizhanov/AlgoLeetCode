# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        
        if root is None:
            return False
        
        q = collections.deque()
        q.append((root,sum - root.val))
        
        while q:
            node,val = q.popleft()
            if not node.left and not node.right:
                if val == 0:
                    return True
            if node.left is not None:
                q.append((node.left,val - node.left.val))
            if node.right is not None:
                q.append((node.right,val - node.right.val))
        
        return False