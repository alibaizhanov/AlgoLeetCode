# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        def lenOfList(List):
            l = 0
            while List:
                l = l+1
                List = List.next
            
            return l
        #############################
        def insertBefore(List,data):
            newNode = ListNode(data)
            
            if List:
                newNode.next = List
            
            return newNode
        #############################
        def padList(List,padding):
            head = List
            for i in range(padding):
                head = insertBefore(head,0)
            
            return head
        
        #############################
        def addTwoLinkedList(l1,l2):
            k = 0
            m = 0
            
            for i in range(len(l1)-1,-1,-1):
                
                summary = l1[i].val + l2[i].val + k
                
                if summary >= 10:
                    k = summary//10
                    m = summary%10
                    summary = m
                else:
                    k=0
                    m=0
                
                l1[i].val = summary
            
            if k>0:
                newL = ListNode(k)
                newL.next = l1[0]
                l1.insert(0,newL)
            
            return l1[0]
        ############################
        
        lenOfl1 = lenOfList(l1)
        lenOfl2 = lenOfList(l2)
        
        
        
        if lenOfl1>lenOfl2:
            l2 = padList(l2,lenOfl1 - lenOfl2)
        else:
            l1 = padList(l1,lenOfl2 - lenOfl1)
            
        newL1,newL2 = [],[]    
        
        
        while l1:
            newL1.append(l1)
            l1 = l1.next
        while l2:
            newL2.append(l2)
            l2 = l2.next
        
        res = addTwoLinkedList(newL1,newL2)
        
        
        return res
                
                    
                    
            
            
        
                
            
        