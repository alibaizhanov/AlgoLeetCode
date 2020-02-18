# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        lenA = 0
        lenB = 0
        tailA = ListNode(0)
        tailB = ListNode(0)
        curA = headA
        curB = headB
        while curA:
            tailA = curA
            curA = curA.next
            lenA = lenA+1
        while curB:
            tailB = curB
            curB = curB.next
            lenB = lenB+1
        
        if tailA != tailB:
            
            return None
        
        if lenA > lenB:
            short =  headB
            long = headA
        else:
            long = headB
            short = headA
        
        diff = abs(lenA-lenB)
        
        while(diff>0 and long):
            long = long.next
            diff = diff-1
        
        while(short!=long):
            
            short = short.next
            long = long.next
        
        return long
            
        
        