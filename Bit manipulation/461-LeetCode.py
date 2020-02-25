##My solution
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        count=0
        for i in bin(x^y):
            if  i == '1':
                count = count + 1
        
        
        return count


#best solution
#https://leetcode.com/problems/hamming-distance/discuss/94697/Python-1-line-49ms