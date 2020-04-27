# Here we use two pointer algorithms
#FSolution algorithms
'''
https://leetcode.com/problems/container-with-most-water/discuss/6099/Yet-another-way-to-see-what-happens-in-the-O(n)-algorithm
https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxarea = 0
        while l<r:
            maxarea = max(maxarea,min(height[l],height[r]) * (r-l))
            if height[l]<height[r]:
                l+=1
            else:
                r-=1
        
        return maxarea
        