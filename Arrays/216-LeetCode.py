###https://leetcode.com/problems/combination-sum-iii/discuss/60805/Easy-to-understand-Python-solution-(backtracking)


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        res=[]
        self.dfs(range(1,10),k,n,0,[],res)
        return res
    
    def dfs(self,nums,k,n,index,path,res):
        if k<0 or n<0:
            return
        if k == 0 and n==0:
            res.append(path)
        
        for i in range(index,len(nums)):
            self.dfs(nums,k-1,n-nums[i],i+1,path+[nums[i]],res)
        