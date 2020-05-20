class Solution(object):
    """
    dictionary

    https://leetcode.com/problems/find-the-difference/discuss/86904/3-Different-Python-Solutions-(Dictionary-Difference-XOR)
    """
    def findTheDifference(self, s, t):
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        for ch in t:
            if dic.get(ch, 0) == 0:
                return ch
            else:
                dic[ch] -= 1