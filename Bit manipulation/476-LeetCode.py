
#My Solution
class Solution:
    def findComplement(self, num: int) -> int:
        bitNum = bin(num).replace("0b","")
        result = ""
        for i in bitNum:
            if i == "1":
                result = result.__add__("0")
            else:
                result = result.__add__("1")
        
        return int(result,2)
#good solution https://leetcode.com/problems/number-complement/discuss/96009/Simple-Python
'''
The core is ^
111 ^ 101 = 010
Then the concern is to let the '0' in num complement to '1', because all the '1' in num will be complemented to "0" with ^.
So how to find the '0's in num
find another number that is one bit left than num and do minus 1.
e.g. 1000 (8) - 1 = 111 (7)
which will be the largest one in that bit-length, only having '1's.
With help of ^, '0' in num now will be complemented to '1'
'''
class Solution(object):
    def findComplement(self, num):
        i = 1
        while i <= num:
            i = i << 1
        return (i - 1) ^ num