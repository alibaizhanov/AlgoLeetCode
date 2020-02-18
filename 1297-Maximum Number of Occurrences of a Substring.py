1297. Maximum Number of Occurrences of a Substring

Given a string s, return the maximum number of ocurrences of any substring under the following rules:

The number of unique characters in the substring must be less than or equal to maxLetters.
The substring size must be between minSize and maxSize inclusive.

import collections
class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        res = collections.Counter(filter(lambda w: len(set(w)) <= maxLetters, (s[i:i + minSize] for i in range(len(s) - minSize + 1)))).most_common(1)
        return res[0][1] if res else 0