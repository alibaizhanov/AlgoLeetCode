# Best solution for this task is use the stack
"""
Here have a good explantion

https://leetcode.com/articles/binary-search-tree-iterator/

"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        
        self.stack = []
        
        self.inorder_left(root)
        
    def inorder_left(self,root):
        
        while root:
            self.stack.append(root)
            root = root.left
        
        

    def next(self) -> int:
        
        """
        @return the next smallest number
        """
        
        topVar = self.stack.pop()
        
        if topVar.right is not None:
            
            self.inorder_left(topVar.right)
        return topVar.val
        

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack)>0
        
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()