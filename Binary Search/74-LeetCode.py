class Solution:
    
    def searchMatrix(self, matrix, target):
        
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        
        n = len(matrix[0])
        lo, hi = 0, len(matrix) * n
        while lo < hi:
            mid = int((lo + hi) / 2)
            x = matrix[int(mid/n)][mid%n]
            if x < target:
                lo = mid + 1
            elif x > target:
                hi = mid
            else:
                return True
        return False
    
    """"
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
       
    
    
        if len(matrix) == 0:
            return False
        if len(matrix[0]) == 0:
            return False
        
        lmat = 0
        hmat = len(matrix)-1
        
        
        while lmat <= hmat:
            mid = int((lmat+hmat)/2)
            
            if matrix[mid][0] == target:
                return True
            
            if matrix[mid][0] > target:
                hmat = mid - 1
            else:
                lmat = mid + 1
            
         
        l = 0
        h = len(matrix[hmat])-1
        
        while l<=h:
            mid = int((l+h)/2)
            
            if matrix[hmat][mid] == target:
                return True
            
            if matrix[hmat][mid] > target:
                h = mid - 1
            else:
                l = mid + 1
        
        
        return False
    """
                
                
        