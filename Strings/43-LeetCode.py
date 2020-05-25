#https://leetcode.com/problems/multiply-strings/discuss/17605/Easiest-JAVA-Solution-with-Graph-Explanation

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        dNum1 = 0
        dNum2 = 0
        
        for i in num1:
            dNum1 = dNum1*10 + int(i)
        
        for j in num2:
            dNum2 = dNum2*10 + int(j)
        
        
        return str(dNum1*dNum2)
        
        