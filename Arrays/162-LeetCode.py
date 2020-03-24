
# binary search, O(log n) time complexity
# https://discuss.leetcode.com/topic/5724/find-the-maximum-by-binary-search-recursion-and-iteration
def findPeakElement(nums):
        
        low = 0
        high = len(nums)-1
        
        while low<high:
            
            mid1 = int((low+high)/2)
            mid2 = mid1+1
            if nums[mid1] < nums[mid2]:
                low = mid2
            else:
                high = mid1
        
        return low
        

print(findPeakElement([1,2,1,3,5,6,4]))