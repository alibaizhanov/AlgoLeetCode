#https://leetcode.com/problems/rotate-image/discuss/18884/Seven-Short-Solutions-(1-to-7-lines)

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        l = len(matrix) - 1
        m = 0
        for i in range(int(len(matrix)/2)):
            a,b = l,l
            c = m
            while b>i:
                t = matrix[a][b]
                matrix[a][b] = matrix[c][a]
                matrix[c][a] = matrix[i][c]
                matrix[i][c] = matrix[b][i]
                matrix[b][i] = t
                
                b = b - 1
                c = c + 1
                
            m = m + 1
            l = l - 1