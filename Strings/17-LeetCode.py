#https://leetcode.com/problems/letter-combinations-of-a-phone-number/discuss/8067/Python-easy-to-understand-backtracking-solution.

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == None:
            return []
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl", "6":"mno", "7":"pqrs", "8":"tuv", "9":"wxyz"}
        res = []
        self.dfs(digits,dic,0,"",res)
        return res
        
        
    def dfs(self,digits,dic,index,path,res):
        
        if len(path)==len(digits):
            res.append(path)
            return
        
        for i in dic[digits[index]]:
            self.dfs(digits,dic,index+1,path+i,res)