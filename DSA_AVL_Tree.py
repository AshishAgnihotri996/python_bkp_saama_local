import DSA_queue_linked_list as queue

class AVLTree:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1


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
    inOrderTraversal(rootNode.leftchild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftchild)
    postOrderTraversal(rootNode.rightchild)
    print(rootNode.data)

def levelOrderTravesal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            root = customQueue.dequeue()
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customQueue.enqueue(root.value.rightchild)

def searchNode(rootNode,nodeValue):
    if rootNode.data == nodeValue:
        print('found')
    elif nodeValue.data <= rootNode.data:
        if rootNode.leftchild.data == nodeValue:
            print('found at leftchild')
        else:
            searchNode(rootNode.leftchild,nodeValue)
    else:
        if nodeValue == rootNode.rightchild.data:
            print('found at rightchild')
        else:
            searchNode(rootNode.rightchild,nodeValue)




newAVL = AVLTree(10)