class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        sumAll = 0
        newArr = sorted(nums)
        length = len(newArr)
        if length%2 != 0:
            newArr.append(0)
        for i in range(0,length,2):
            sumAll = sumAll + min(newArr[i],newArr[i+1])
        
        return sumAll