#https://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        
        if len(matrix) == 0:
            return []
        
        res = []
        m = len(matrix)
        n = len(matrix[0])
        
        
        self.spiralPrint(m,n,matrix,res)
        
        return res
        
    def spiralPrint(self,m, n, a,res) : 
        k = 0 
        l = 0
        while k < m and l < n :
            # Print the first row from 
            # the remaining rows  
            for i in range(l, n) : 
                res.append(a[k][i])

            k += 1
            # Print the last column from 
            # the remaining columns  
            for i in range(k, m) : 
                res.append(a[i][n - 1]) 

            n -= 1

            # Print the last row from 
            # the remaining rows  
            if k < m: 

                for i in range(n - 1, (l - 1), -1) : 
                    res.append(a[m - 1][i]) 

                m -= 1

            # Print the first column from 
            # the remaining columns  
            if l < n: 
                for i in range(m - 1, k - 1, -1) : 
                    res.append(a[i][l])

                l += 1
        