from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        rList = []
        tCount = Counter(i for i in nums)
        
        def maxKeyVal(dictCount):
            maxKey = 0
            maxVal = 0
            for key,value in dictCount.items():
                if value > maxVal:
                    maxVal = value
                    maxKey = key
            
            return maxKey
         
        for i in range(k):
            
            maxV = maxKeyVal(tCount)
            rList.append(maxV)
            tCount.pop(maxV)
        
        return rList