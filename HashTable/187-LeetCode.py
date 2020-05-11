class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if 10>len(s):
            return []
        
        d = {}
        res = []
        
        for i in range(len(s)-9):
            if d.get(s[i:i+10]) == None:
                d[s[i:i+10]] = 1
            else:
                d[s[i:i+10]] = d[s[i:i+10]] + 1
        
        
        for k,v in d.items():
            if v > 1:
                res.append(k)
        
        
        return res
        