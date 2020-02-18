# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
            
            if head is None:
                
                return head
            
            l = 0
            
            copyHead = head
            
            while copyHead is not None:
                
                copyHead = copyHead.next
                l = l + 1
                
            copyHead = head
            
            if l==n:
                
                return head.next
            
            while head is not None:
                
                if l != n:
                    l = l-1
                    temp = head
                    head = head.next
                    continue
                else:
                    temp.next = head.next
                    break
                
            return copyHead