class Solution:
    def isValid(self, s: str) -> bool:
        
        d = {')':'(',']':'[','}':'{'}
        stack = ["N"]
        
        for i in s:
            if i in d.keys():
                if stack.pop() != d[i]:
                    return False
            else:
                stack.append(i)
        
        return len(stack)==1
    