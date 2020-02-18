##My algo
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        plusOne = digits[-1] + 1
        
        if plusOne >= 10:
            
            digits[-1] = plusOne%10
            rOne = plusOne//10
            
            for i in range(len(digits)-2,-1,-1):
                
                resOne = digits[i] + rOne
                
                if resOne >= 10:
                    
                    digits[i] = resOne%10
                    rOne = resOne//10
                    
                else:
                    digits[i] = resOne
                    rOne = 0
            
            if rOne != 0:
                
                digits.insert(0,rOne)
                    
        else:
            
            digits[-1] = plusOne
        
        return digits

#Best algo

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        l = len(digits)
        
        for i in range(l-1,-1,-1):
            
            if digits[i]<9:
                
                digits[i] = digits[i] + 1
                
                return digits
            else:
                
                digits[i] = 0
        
        digits.insert(0,1)
        
        return digits
        