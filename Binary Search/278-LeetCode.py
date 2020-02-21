# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

'''
It's my solution and i think is good solution
Here i use Binary Search algorithm 

'''

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 0
        high = n
        
        res = 0
        
        while low<=high:
            
            mid = int((low + high)/2)
            
            if isBadVersion(mid) == True:
                res = mid
                high = mid-1
            else:
                low = mid+1
        
        return res