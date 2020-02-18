# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        
        if head is None:
            
            return head
        
        low = []
        high = []
        
        while head:
            if head.val >=x:
                high.append(head)
            else:
                low.append(head)
            
            head = head.next
            
        if len(low) > 0:
            
            for i in range(len(low)-1):
                
                 low[i].next = low[i+1]
            
            if len(high)> 0:
                
                low[-1].next = high[0]
                
        if len(high) > 0:
            
            for i in range(len(high)-1):
                
                high[i].next = high[i+1]
            
            high[-1].next = None
        
        
        if len(low)>0:
            
            return low[0]
        
        else:
            
            return high[0]
        
            
        
        
            
        
        
        