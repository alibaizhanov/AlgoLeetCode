class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        res = collections.Counter(s)
        
        for k,v in res.items():
            if v == 1:
                return s.find(k)
        
        
        return -1