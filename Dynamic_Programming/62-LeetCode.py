##https://leetcode.com/problems/unique-paths/discuss/22975/Python-easy-to-understand-solutions-(math-dp-O(m*n)-and-O(n)-space).
#Both solutions it's my solutions

class Solution:
    """
    def __init__(self):
        
        self.mDict = {}
        
    def uniquePaths(self, m: int, n: int) -> int:
        
        if m==1 or n == 1:
            return 1
        
        if self.mDict.get(str(m) + ":" + str(n)) != None:
            
            return self.mDict.get(str(m) + ":" + str(n))
            
        
        res = self.uniquePaths(m-1,n) + self.uniquePaths(m,n-1)
        self.mDict[str(m) + ":" + str(n)] = res
        return res
    """
    def uniquePaths(self, m: int, n: int) -> int:
        
        rList= [[0] * m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                if i == 0 or j == 0:
                    rList[i][j] = 1
                else:
                    rList[i][j] = rList[i][j-1] + rList[i-1][j]
        
        return rList[n-1][m-1]
    
        