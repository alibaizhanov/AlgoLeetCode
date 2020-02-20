'''
good explanation 
https://leetcode.com/problems/excel-sheet-column-title/discuss/51404/Python-solution-with-explanation
// https://discuss.leetcode.com/topic/35360/my-easy-to-understand-java-solution/4

'''


class Solution:
    def convertToTitle(self, num: int) -> str:
        capitals = [chr(x) for x in range(ord('A'), ord('Z')+1)]
        result = []
        
        while num > 0:
            result.append(capitals[(num-1)%26])
            num = (num-1) // 26
        result.reverse()
        
        return ''.join(result)