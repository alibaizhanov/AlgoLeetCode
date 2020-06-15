#My Solution
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#I think is best solution https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/discuss/33834/Python-simple-BFS
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        
        q = collections.deque()
        res = []
        q.append((root,1))
        while q:
            node,level = q.popleft()
            if len(res) < level:
                res.append([])
            if level%2 != 0:
                res[level-1].append(node.val)
            else:
                res[level-1].insert(0,node.val)
                
            
            if node.left is not None:
                q.append((node.left,level+1))
            if node.right is not None:
                q.append((node.right,level+1))
        return res
            