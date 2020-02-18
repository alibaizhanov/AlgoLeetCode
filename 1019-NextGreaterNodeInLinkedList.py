# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        queue = []
        while head:
            queue.append(head.val)
            head = head.next
        
        stack = [] # store the increasing index, who's value is decreasing
        res = []
        for i, val in enumerate(queue):
            while stack and val > queue[stack[-1]]:
                res[stack[-1]] = val
                stack.pop()
                
            stack.append(i)
            res.append(0)
            
        return res
        