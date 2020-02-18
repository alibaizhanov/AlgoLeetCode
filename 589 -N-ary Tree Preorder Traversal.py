"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        result = []
        
        if not root:
            return None
        
        def recurse(root):
            if not root:
                return
            result.append(root.val)
            for child in root.children:
                recurse(child)
                
        recurse(root)
        return result
"""

# iterative
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        result, stack = [], []
        
        if not root:
            return None
        stack.append(root)
        while stack:
            root = stack.pop()
            result.append(root.val)
            stack.extend(reversed(root.children))
        return result
"""