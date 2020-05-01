##(Explanation) Here i used stack for each step and append to stack if we take symbol like + pop last and pop later

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operDict = {"+":"+","-":"-","*":"*","/":"/"}
        
        for token in tokens:
            
            if operDict.get(token) != None:
                t1 = stack.pop()
                t2 = stack.pop()
                
                if operDict.get(token) == "+":
                    stack.append(t2 + t1)
                elif operDict.get(token) == "-":
                    stack.append(t2 - t1)
                elif operDict.get(token) == "*":
                    stack.append(t2 * t1)
                else:
                    stack.append(int(t2/t1))
            else:
                
                stack.append(int(token))
        
        return stack[-1]
                    