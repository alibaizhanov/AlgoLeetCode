import re
class Solution:
    def isPalindrome(self, s):
	    s = re.sub('[^0-9a-z]+', '', s.lower())
	    return s == s[::-1]