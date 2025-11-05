class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insertNode(self,word):
        current = self.root
        for i in word:
            ch  = i
            node = current.children.get(ch)
            if node == None:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print('inserted sucscessfully')

    def searchString(self,word):
        currentNode = self.root
        for i in word:
            node = currentNode.children.get(i)
            if node == None:
                return False
            currentNode = node
        if currentNode.endOfString == True:
            return True
        else:
            return False

    def insertWord(self,index,word):


newTrie = Trie()
newTrie.insertNode('AAP')
print(newTrie.searchString('AaAP'))