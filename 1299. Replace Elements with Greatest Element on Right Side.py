class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        res = [-1]*len(arr)
        for i in range(len(arr)-1,0,-1):
            res[i-1] = max(res[i], arr[i])
        return res