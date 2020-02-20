'''
     Time complexity O(1), space complexity O(1)
     Explanation
     https://discuss.leetcode.com/topic/47983/java-dp-o-1-solution
     https://discuss.leetcode.com/topic/48332/java-o-1-with-explanation
     My explanation:
     n==0 -> 1
     n==1 -> (0 <= x < 10) -> 10
     n==2 -> (0 <= x < 10) + (10 <= x < 100) -> 10 + 9*9
     why 9*9:
      1st digit - can be [1..9] = 9, because of it can`t be 0.
      2nd digit - can be [0..9] excluding 1st => 9
     n==3 -> (0 <= x < 10) + (10 <= x < 100) + (100 <= x < 1000) -> 10 + 9*9 + 9*9*8
     why 9*9*8:
      1st digit - can be [1..9] = 9, because of it can`t be 0.
      2nd digit - can be [0..9] excluding 1st => 9
      3nd digit - can be [0..9] excluding 1st & 2nd => 8
     ...
     ...
     n==10 -> (0 <= x < 10) + (10 <= x < 100) ... (10^9 <= x < 10^10)
     (10^9 <= x < 10^10) => 9*9*8.....*2*1
     n==11 -> (0 <= x < 10) + (10 <= x < 100) ... (10^10 <= x < 10^11)
     (10^10 <= x < 10^11) => 9*9*8.....*2*1*0 = 0
     So the max number of unique numbers is the same like n==10 even n>10.
     This is obvious, because such numbers has more than 10 digits,
     thus some digit used at least twice.
'''

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0:
            return 1
        sum = 10
        mul = 9
        
        if n>10:
            n = 10
        
        for i in range(n-1):
            
            mul = mul * (9-i)
            sum = sum + mul
        
        
        return sum