Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: [1,3,5,6], 5
Output: 2
Example 2:

Input: [1,3,5,6], 2
Output: 1
Example 3:

Input: [1,3,5,6], 7
Output: 4
Example 4:

Input: [1,3,5,6], 0
Output: 0

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        f = 0
        l = len(nums) - 1
        while f <= l:
            t =int((l+f)/2)
            if nums[t] == target:
                return t
                break
            elif nums[t] > target:
                l = t - 1
            else:
                f = t + 1
        if f == len(nums):
            f = f-1        
        if nums[f] > target and f==0:
            return 0
        elif nums[f] > target and f!=0:
            return f
        else:
            return f+1