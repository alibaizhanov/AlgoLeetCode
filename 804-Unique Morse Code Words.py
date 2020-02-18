class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        l = len(alpha)
        alphaMorse = dict()
        result = list()
        
        for i in range(l):
            
            alphaMorse[alpha[i]] = morse[i]
        
        for word in words:
            
            m = ""
            
            for letter in word:
                
                m = m + alphaMorse.get(letter)
            
            result.append(m)
        
        return set(result).__len__()
                
        
        