class Solution:
    def reverseWords(self, s: str) -> str:
        
        return " ".join(list(filter(lambda st: st!="",s.strip().split(" ")))[::-1])