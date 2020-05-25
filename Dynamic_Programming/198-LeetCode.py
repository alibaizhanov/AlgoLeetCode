class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # Approach 1:- Construct dp table
        if not nums: 
            return 0
        if len(nums) == 1: 
            return nums[0]

        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return dp[-1] # return the last element
        
        """ 
        #My Solution
        if len(nums)<=2:
            if len(nums) == 0:
                return 0
            else:
                return max(nums)
        
        
        for i in range(2,len(nums)):
            nums[i] = nums[i] + max(nums[0:i-1])
        
        
        return max(nums)
        """