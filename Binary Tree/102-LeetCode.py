# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
#Here we use BFS traversal method and for space used dictionary
#Iteratively
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        
        if root is None:
            return []
        
        squeue = []
        squeue.append((root,0))
        res = {}
        
        while squeue:
            node,level = squeue.pop(0)
            if res.get(level) != None:
                res[level].append(node.val)
            else:
                res[level] = [node.val]
            if node.left:
                squeue.append((node.left,level+1))
            if node.right:
                squeue.append((node.right,level+1))
            
        
        return [i for i in res.values()]
        
"""
#Recursively
class Solution(object):
    def levelOrder(self, root):
        result = []
        self.helper(root, 0, result)
        return result
    
    def helper(self, root, level, result):
        if root is None:
            return
        if len(result) <= level:
            result.append([])
        result[level].append(root.val)
        self.helper(root.left, level+1, result)
        self.helper(root.right, level+1, result)
