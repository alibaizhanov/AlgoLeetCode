'''
172. Factorial Trailing Zeroes
https://leetcode.com/problems/factorial-trailing-zeroes/
Given an integer n, return the number of trailing zeroes in n!.
Note: Your solution should be in logarithmic time complexity.
Credits:
Special thanks to @ts for adding this problem and creating all Snake_3 cases.
Subscribe to see which companies asked this question
'''

class Solution:
    def trailingZeroes(self, n: int) -> int:
        
       
        i = 2
        ost = n//5
        res= ost
        
        while ost > 0:
            c = 5**i
            ost = n//c
            res = res + ost
            i = i + 1
            
        return res
        