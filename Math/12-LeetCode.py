class Solution:
    def intToRoman(self, num):
        values = [ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 ]
        numerals = [ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" ]
        res, i = "", 0
        while num:
            res += (num//values[i]) * numerals[i]
            num %= values[i]
            i += 1
        return res
    """
    #It's best solution
    def intToRoman(self, num: int) -> str:
        if num > 3999:
            return None
        romDic = [(1,"I"),(4,"IV"),(5,"V"),(9,"IX"),(10,"X"),(40,"XL"),(50,"L"),(90,"XC"),(100,"C"),(400,"CD"),(500,"D"),(900,"CM"),(1000,"M"),(4000,"MMM")]
        
        resN = 0
        resS =  []
        for i in range(len(romDic)):
            
            n,s = romDic[i]
            
            if  n == num:
                return s
            
            if num < n:
                j = i-1
                
                while j>=0:
                    nVal,sVal = romDic[j]
                    resN = resN + nVal
                    resS.append(sVal)
                    
                    if resN == num:
                        return "".join(resS)
                    
                    if resN > num:
                        j = j -1
                        resN = resN-nVal
                        resS.pop()
    """
                    
                    
                    
                    
                    
                    
        
        
        