# How to find out inner reactangle
# https://ru.stackoverflow.com/questions/758529/%D0%9F%D0%B5%D1%80%D0%B5%D1%81%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D0%B5-%D0%B4%D0%B2%D1%83%D1%85-%D0%BF%D1%80%D1%8F%D0%BC%D0%BE%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA%D0%BE%D0%B2-c

class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        
        
        rect1l = C-A
        rect1h = D-B
        
        rect2l = G-E
        rect2h = H-F
        
        squareRect1 = rect1l*rect1h
        squareRect2 = rect2l*rect2h
        
        innerLeft = max(A,E)
        innerRight = min(C,G)
        innerTop = min(D,H)
        innerBottom = max(B,F)
        
        
        innerWidth = innerRight - innerLeft
        innerHeight = innerTop - innerBottom
        innerSquare = 0
        
        if innerWidth > 0 and innerHeight>0:
            innerSquare = innerWidth * innerHeight
            
        
        res = (squareRect1+squareRect2) - innerSquare
        
        return res