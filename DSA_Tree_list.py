class Tree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastuseIndex = 0
        self.maxSize = size

    def insertNode(self,node):
        if self.lastuseIndex + 1 ==self.maxSize:
            return 'the binary tree is full'
        self.customList[self.lastuseIndex+1] = node
        self.lastuseIndex += 1
        return 'inserted successfully'

    def searchNode(self,value):
        for i in range(len(self.customList)):
            if self.customList[i] == value:
                return 'success'
        return 'failed'

    def preOrderTraversal(self,index):
        if index > self.lastuseIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index *2)
        self.preOrderTraversal(index *2+1)

    def inorderTraversal(self,index):
        if index > self.lastuseIndex:
            return
        self.inorderTraversal(index *2 )
        print(self.customList[list])
        self.inorderTraversal(index * 2+1)

    def postOrderTraversal(self,index):
        if index > self.lastuseIndex:
            return
        self.postOrderTraversal(index * 2)
        self.postOrderTraversal(index * 2+1)
        print(self.customList[index])

    def levelOrderTravsal(self,index):
        for i in range(index,self.lastuseIndex):
            print(self.customList[i])

    def deleteNode(self,value):
        if self.lastuseIndex == 0:
            return
        for i in range(1, self.lastuseIndex +1):
           if self.customList[i] == value:
               self.customList[i] = self.customList[self.lastuseIndex]
               self.customList[self.lastuseIndex] =None
               self.lastuseIndex -=1
               return 'the node has been deleted successfully'

    def deleteEntireTree(self):
        self.customList = None
        return 'all nodes have been delted successfully'


newBT = Tree(8)
print(newBT.insertNode('drinks'))
print(newBT.insertNode('hot'))
print(newBT.insertNode('cold'))
print(newBT.insertNode('tea'))
print(newBT.insertNode('coffee'))
# print(newBT.searchNode('cold'))
newBT.preOrderTraversal(1)