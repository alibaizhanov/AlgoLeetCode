# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Explanation:

Here i had used dfs algorithm and first  dfs algorithm help us to find maximum depth of our tree 
and then i used BFS algorithm with queue, here queue help us traverse the tree iteratively, 
in the second algorithm we used while loop in order to fill stack and that same time pick up left and right side of our tree and add to stack untill the stack will be emplty
and in the while loop we have a condition which checks each node and if node level equals to maximum depth of our tree then we add to node value to the sum variable
 and in the end of our function we just return the sum

"""

class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        
        if not root:
            return 0
    
        stackDq = [(root,1)]
        maxDp = self.dfsDepth(root)
        sum = 0
        
        while len(stackDq)!=0:
            
            node,level = stackDq.pop(0)
            
            if level == maxDp:
                sum = sum + node.val
            
            if node.left is not None:
                stackDq.append((node.left,level+1))
            
            if node.right is not None:
                stackDq.append((node.right,level+1))
            
        return sum
            
    def dfsDepth(self,root):
        if root is None: 
            return 0 ;  
  
        else : 
            # Compute the depth of each subtree 
            lDepth = self.dfsDepth(root.left) 
            rDepth = self.dfsDepth(root.right) 

            # Use the larger one 
            if (lDepth > rDepth): 
                return lDepth+1
            else: 
                return rDepth+1