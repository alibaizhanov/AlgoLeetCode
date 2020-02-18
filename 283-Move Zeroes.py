class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        i=0
        j=0
        
        while i < l:
            if nums[j] == 0:
                tempVal = nums.pop(j)
                nums.append(tempVal)
            else:
                j = j + 1
            
            i = i + 1