#Explanation

"""

Here first i use python function which called bin() in order to convert int value to the bin value
then bin() return str and i cutted 0b in bin value then, used algorithm for palindromic problem

"""

class Solution:
    def reverseBits(self, n: int) -> int:
        
        bStr = bin(n).replace("0b","")
        ls = list(bStr.rjust(32,"0"))
        
        
        l = 0
        h = len(ls)-1
        
        while l<h:
            temp = ls[l]
            ls[l] = ls[h]
            ls[h] = temp
            l = l + 1
            h = h - 1
        
        
        return int("".join(ls),2)