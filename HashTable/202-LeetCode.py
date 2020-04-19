class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<0:
            return False
        
        def digitSum(n):
            res=0
            while n>0:
                reminder = n%10
                res = res + reminder**2
                n=n//10
            return res
        
        while True:
            
            result = digitSum(n)
            
            if result == 1:
                return True
            
            n = result
                
            
            