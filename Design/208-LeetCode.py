class TrieNode: 
      
    # Trie node class 
    def __init__(self): 
        self.children = [None]*26
        
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.root = self.getNode() 

    def getNode(self):
        
        return TrieNode() 
    
    def _charToIndex(self,ch):
        
        return ord(ch)-ord('a') 
        

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """

        pCrawl = self.root 
        length = len(word) 
        for level in range(length): 
            index = self._charToIndex(word[level]) 
            
            if not pCrawl.children[index]: 
                pCrawl.children[index] = self.getNode() 
            pCrawl = pCrawl.children[index] 
            
        pCrawl.isEndOfWord = True
                
        

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        pCrawl = self.root 
        length = len(word) 
        for level in range(length): 
            index = self._charToIndex(word[level]) 
            if not pCrawl.children[index]: 
                return False
            pCrawl = pCrawl.children[index] 
            
        return pCrawl != None and pCrawl.isEndOfWord 
        

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        pCrawl = self.root 
        length = len(prefix) 
        for level in range(length): 
            index = self._charToIndex(prefix[level]) 
            if not pCrawl.children[index]: 
                return False
            pCrawl = pCrawl.children[index] 
            
        return pCrawl != None
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)