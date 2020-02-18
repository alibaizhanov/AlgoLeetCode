# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
     
        tempArray = list()
        
        while head is not None:
            
            tempArray.append(head)
            
            head = head.next
            
        st = 0
        ls = len(tempArray)-1
        
        if len(tempArray) <= 2:
            
            return head
        
        while st < ls:
            
            tempArray[st].next = tempArray[ls]
            tempArray[ls].next = tempArray[st + 1]
            tempArray[st + 1].next = None
            
            
            st = st + 1
            ls = ls - 1 
        
        return tempArray[0]
            