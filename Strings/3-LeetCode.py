"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        maxnum,num,ss =0,0,''
        for each in s:
            if each in ss:
                ss = ss.split(each)[-1]+each
                num =len(ss)
            else:
                num += 1
                ss += each
                if num>=maxnum:
                    maxnum = num

        return maxnum
"""
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic, res, start, = {}, 0, 0
        for i, ch in enumerate(s):
            # when char already in dictionary
            if ch in dic:
                # check length from start of string to index
                res = max(res, i-start)
                # update start of string index to the next index
                start = max(start, dic[ch]+1)
            # add/update char to/of dictionary 
            dic[ch] = i
        # answer is either in the begining/middle OR some mid to the end of string
        return max(res, len(s)-start)
        