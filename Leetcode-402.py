# [402. Remove K Digits](https://leetcode-cn.com/problems/remove-k-digits/)


class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res = ""
        if k == 0:
            return num
        if k == len(num):
            return "0"

        length = len(num)
        remlen = length-k-1
        st = 0

        for i in range(length-k):
            curstr = num[st:length-remlen]
            idx = 0
            curch = curstr[0]
            for i in range(len(curstr)):
                if ord(curstr[i]) < ord(curch):
                    curch = curstr[i]
                    idx = i
            res += curstr[idx]
            st += idx+1
            remlen -= 1
        return str(int(res))




## Code2

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return "0"
        for i in range(k):
            flag = False
            for k in range(1,len(num)):
                if ord(num[k])<ord(num[k-1]):
                    flag = True
                    num = num[:k-1]+num[k:]
                    break
            if not flag:
                num = num[:-1]
        return str(int(num))

