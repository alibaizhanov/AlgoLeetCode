class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        if n == 1:
            return True
        if n%2==0:
            for i in range(n):
                t = 2<<i
                
                if t == n:
                    return True
                if t > n:
                    return False
        else:
            return False
            
        return False