class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        
        for i in range(len(nums)):
            for j in range(len(res)):
                if sorted(res[j] + [nums[i]]) not in res:
                    res.append(sorted(res[j] + [nums[i]]))
        
        return res
                