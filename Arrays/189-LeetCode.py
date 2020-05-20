class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        
        """
        Do not return anything, modify nums in-place instead.
        """
        
        #l = len(nums)
        #nums[:] = nums[l-k:l]+nums[0:l-k]
        ####################################
        n = len(nums)
        k = k % n
        nums[:] = nums[n-k:] + nums[:n-k]