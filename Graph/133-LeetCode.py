"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution(object):
    
    def __init__(self):
        self.visited = {}
        
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return
        
        if node.val in self.visited:
            return self.visited[node.val]
        
        cNode = Node(node.val)
        self.visited[node.val] = cNode
        
        
        for i in node.neighbors:
            cNode.neighbors.append(self.cloneGraph(i))
        
        
        return cNode
        
                