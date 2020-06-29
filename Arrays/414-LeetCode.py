class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if len(set(nums))<3:
            return max(nums)
        
        max1 = float("-inf")
        max2 = float("-inf")
        max3 = float("-inf")
        
        for num in nums:
            
            if num>max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif max2<num<max1:
                max3 = max2
                max2 = num
            elif max3<num<max2:
                max3 = num
        
        return max3