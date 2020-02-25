#it's my version i think this have a good solution for that problems
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        aList = list(a)
        bList = list(b)
        y = 0
        
        if len(a) > len(b):
            dif = len(a) - len(b)
            l = len(a)
            for i in range(dif):
                bList.insert(0,0)
        else:
            dif = len(b) - len(a) 
            l = len(b)
            for i in range(dif):
                aList.insert(0,0)
        
        for i in range(l-1,-1,-1):
            
            temp = int(aList[i]) + int(bList[i]) + y
            
            if temp == 2:
                aList[i] = str(0)
                y = 1
            elif temp == 3:
                aList[i] = str(1)
                y = 1
            else:
                aList[i] = str(temp)
                y=0
            
        if y!=0:
            
            aList.insert(0,str(y))
        
        return "".join(aList)

# Good solution
# https://discuss.leetcode.com/topic/13698/short-ac-solution-in-java-with-explanation/2