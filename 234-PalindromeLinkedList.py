# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        
        """
        #My version Baizhanov Ali
        tempList = list()
        while head is not None:
            
            tempList.append(head.val)
            head = head.next
           
        r = "".join(map(str,tempList[::-1]))
        l = "".join(map(str,tempList))
        
        if r == l:
            return True
        else:
            return False
        """
        fast = head
        slow = head
        stack = list()
        
        while(fast and fast.next):
            
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        if fast:
            slow = slow.next
        
        while slow:
            
            top = stack.pop()
            
            if top!=slow.val:
                return False
            
            slow = slow.next
        
        return True
                
            
            
        