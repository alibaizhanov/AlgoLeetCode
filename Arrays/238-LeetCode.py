class Solution:
        
    #https://leetcode.com/problems/product-of-array-except-self/discuss/65622/Simple-Java-solution-in-O(n)-without-extra-space
        
    def productExceptSelf(self, nums):
            p = 1
            n = len(nums)
            output = []
            for i in range(0,n):
                output.append(p)
                p = p * nums[i]
            p = 1
            for i in range(n-1,-1,-1):
                output[i] = output[i] * p
                p = p * nums[i]
            return output