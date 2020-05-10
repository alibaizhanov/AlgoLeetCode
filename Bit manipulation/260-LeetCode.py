#Good explanation 
#https://leetcode.com/problems/single-number-iii/discuss/68900/Accepted-C%2B%2BJava-O(n)-time-O(1)-space-Easy-Solution-with-Detail-Explanations

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        
        d = collections.Counter(nums)
        res = []
        
        for k,v in d.items():
            if v == 1:
                res.append(k)
        
        
        return res