class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        for i in range(len(board)):
            for j in range(len(board[i])):
                
                if self.dfs(board,i,j,word):
                    return True
        
        return False
                    
        
    def dfs(self,board,i,j,word):
        
        if len(word) == 0: # all the characters are checked
            return True
        
        if (i<0 or i>=len(board) or j<0 or j>=len(board[i]) or board[i][j] != word[0]):
            return False
        
        tmp = board[i][j]  # first character is found, check the remaining part
        board[i][j] = "#"  # avoid visit agian 
            
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
              or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        
        return res