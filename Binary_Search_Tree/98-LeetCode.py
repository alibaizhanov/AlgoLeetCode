# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


#Best Explanation 
# https://leetcode.com/problems/validate-binary-search-tree/discuss/146601/Python3-100-using-easy-recursion
class Solution:
    def isValidBST(self, root):
        return self.check_bst(root, float("-inf"), float("inf"))

    def check_bst(self, node, left, right):
        if not node:
            return True

        if not left < node.val < right:
            return False

        return (self.check_bst(node.left, left, node.val)
                and self.check_bst(node.right, node.val, right))
                
            
        
    
    """
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        return self.dfs(root,root.val)
    
    def dfs(self,root,rootVal):
        
        if not root:
            return True
        
        if root.right is not None and root.val >= root.right.val:
            return False
        if root.left is not None and root.val <= root.left.val:
            return False
        
        self.dfs(root.left,rootVal)
        self.dfs(root.right,rootVal)
        
        return True
    """
        