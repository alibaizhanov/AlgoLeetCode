#My Solution

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        if obstacleGrid[0][0] == 1:
            return 0
        
        n = len(obstacleGrid)
        m = len(obstacleGrid[0])

        for i in range(n):
            num = 1
            for j in range(m):
                if i == 0 or j == 0:
                    if i == 0 and j>0 and (obstacleGrid[i][j] == 1 or obstacleGrid[i][j-1] == 0):
                        obstacleGrid[i][j] = 0
                    elif j == 0 and i>0 and (obstacleGrid[i][j] == 1 or obstacleGrid[i-1][j] == 0):
                        obstacleGrid[i][j] = 0
                    else:
                        obstacleGrid[i][j] = 1
                else:
                    if obstacleGrid[i][j] != 1:
                        obstacleGrid[i][j] = obstacleGrid[i][j-1] + obstacleGrid[i-1][j]
                    else:
                        obstacleGrid[i][j] = 0
        return obstacleGrid[n-1][m-1]