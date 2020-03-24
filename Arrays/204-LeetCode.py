#My Solution
class Solution:
    def countPrimes(self, n: int) -> int:
        
        newDict = [0]*n
        count = 0
        
        for i in range(2,n):
                
            for j in range(i,n):
                
                temp = i*j
                
                if temp < n:
                    
                    newDict[temp] = 1
                else:
                    break
            
            if newDict[i] == 0:
                
                count = count + 1

        return count
##Best solution https://leetcode.com/problems/count-primes/discuss/57595/Fast-Python-Solution
class Solution:
# @param {integer} n
# @return {integer}
def countPrimes(self, n):
    if n < 3:
        return 0
    primes = [True] * n
    primes[0] = primes[1] = False
    for i in range(2, int(n ** 0.5) + 1):
        if primes[i]:
            primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
    return sum(primes)