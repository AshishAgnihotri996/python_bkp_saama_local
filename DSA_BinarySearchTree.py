import DSA_queue_linked_list as queue


class Tree:
    def __init__(self,data):
        self.data= data
        self.leftchild = None
        self.rightchild = None

def insertNode(rootNode,nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftchild is None:
            rootNode.leftchild = Tree(nodeValue)
        else:
            insertNode(rootNode.leftchild, nodeValue)
    else:
        if rootNode.rightchild is None:
            rootNode.rightchild = Tree(nodeValue)
        else:
            insertNode(rootNode.rightchild,nodeValue)
    return 'inserted successfully'


def preOrderTraversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrderTraversal(rootNode.leftchild)
    preOrderTraversal(rootNode.rightchild)

def inOrderTraversal(rootNode):
    if not rootNode:
        return
    inOrderTraversal(rootNode.leftchild)
    print(rootNode.data)
    inOrderTraversal(rootNode.rightchild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)

def levelOrderTraversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftchild is None:
                customQueue.enqueue(root.value.leftchild)
            if root.value.rightchild is None:
                customQueue.enqueue(root.value.rightchild)

def searchNode(rootNode,value):
    if rootNode.data == value:
        print('value found')
    elif value < rootNode.data:
        if rootNode.leftchild.data == value:
            print('value found')
        else:
            searchNode(rootNode.leftchild,value)
    elif value > rootNode.data:
        if rootNode.rightchild.data == value:
            print('node found')
        else:
            searchNode(rootNode.rightchild,value)

def minvalueMethod(Tree):
    current = Tree
    while current.leftchild is not None:
        current = current.leftchild
    return currenty

def deleteNode(rootNode,value):
    if rootNode is None:
        return
    if value < rootNode.data:
        rootNode.leftchild = deleteNode(rootNode.leftchild, value)
    elif value > rootNode.data:
        rootNode.rightchild = deleteNode(rootNode.rightchild,value)

    else:
        if rootNode.rightchild is None:
            temp = rootNode.leftchild
            rootNode = None
            return temp

        if rootNode.leftchild is None:
            temp = rootNode.leftchild
            rootNode = None
            return temp
    temp = minvalueMethod(rootNode.rightchild)
    rootNode.data =temp.data
    rootNode.rightchild = minvalueMethod(rootNode.rightchild, temp.data)


def deleteAll(rootNode):
    rootNode.data = None
    rootNode.leftchild = None
    rootNode.rightchild = None
    return 'the bst has been successfullly delted'

newBST = Tree(None)
print(insertNode(newBST,70))
print(insertNode(newBST,60))
# print(insertNode(newBST,70))
print(newBST.data)
print(newBST.leftchild.data)
# print(searchNode(newBST,60))
deleteNode(newBST,60)
