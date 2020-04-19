# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def middleNode(self, head):
        tmp = head
        while tmp and tmp.next:
            head = head.next
            tmp = tmp.next.next
        return head

##Explanation
'''
We need two pointers, one is head with one step each iteration, 
and the other is tmp with two steps each iteration. 
So when the tmp reaches the end of the list, 
the head just reaches the half of it, which is exactly what we want.

And one thing needs to be considered additionaly is that the number of the node can be odd and even, 
which may affect the termination condition of the iteration. 
To solve this, my idea is to try the algorithm in some small set of the examples, 
like the examples provided by the official. And you will find that if the tmp reaches Null or tmp.next reaches Null, 
the head is the result.
