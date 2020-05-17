class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        zeroMat = []
        
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    zeroMat.append([i,j])
        
        for pair in zeroMat:
            self.rowUpdate(matrix,pair[0])
            self.columnUpdate(matrix,pair[1])
            
    
    
    def rowUpdate(self,matrix,i):
        for j in range(len(matrix[i])):
            matrix[i][j] = 0
    
    def columnUpdate(self,matrix,j):
        for i in range(len(matrix)):
            matrix[i][j] = 0
            