#simple tree example

# class TreenNode:
#     def __init__(self,data,children =[]):
#         self.data = data
#         self.children = children
#
#     def __str__(self,level = 0):
#         ret = " " * level + str(self.data) + '\n '
#         for child in self.children:
#             ret += child.__str__(level+1)
#         return ret
#
#     def addChild(self,TreeNode):
#         self.children.append(TreeNode)
#
# tree = TreenNode('drinks',[])
# cold = TreenNode('cold',[])
# hot = TreenNode('hot',[])
# tree.addChild(cold)
# tree.addChild(hot)
# tea = TreenNode('tea',[])
# coffee = TreenNode('tea',[])
# fanta = TreenNode('fanta',[])
# cola = TreenNode('cola',[])
# cold.addChild(cola)
# cola.addChild(fanta)
# hot.addChild(tea)
# hot.addChild(coffee)
# print(tree)


#creation of binary tree in terms of linked list

# import DSA_queue_linked_list as queue
#
#
# class TreeNode:
#     def __init__(self,data):
#         self.data = data
#         self.leftchild = None
#         self.rightchild = None
#
# newBT = TreeNode('drinks')
# leftchild = TreeNode('hot')
# tea = TreeNode('tea')
# coffee = TreeNode('coffee')
# leftchild.leftchild = tea
# leftchild.leftchild = coffee
# rightchild = TreeNode('cold')
# newBT.leftchild = leftchild
# newBT.rightchild = rightchild
#
# def preorderTraversal(rootnode):
#     if rootnode is None:
#         return
#     print(rootnode.data)
#     preorderTraversal(rootnode.leftchild)
#     preorderTraversal(rootnode.rightchild)
# preorderTraversal(newBT)
#
# def inorderTraversal(rootnode):
#     if not rootnode:
#         return
#     inorderTraversal(rootnode.leftchild)
#     print(rootnode.data)
#     inorderTraversal(rootnode.rightchild)
# inorderTraversal(newBT)
#
# def postOrdertraversal(rootnode):
#     if not rootnode:
#         return
#     else:
#         postOrdertraversal(rootnode.rightchild)
#         postOrdertraversal(rootnode.leftchild)
#         print(rootnode.data)
# postOrdertraversal(newBT)
#
#
# def levelOrderTraversal(rootNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not customQueue.isEmpty():
#             root = customQueue.dequeue()
#             print(root.value.data)
#             if (root.value.leftchild is not None):
#                 customQueue.enqueue(root.value.leftchild)
#             if (root.value.rightchild is not None):
#                 customQueue.enqueue(root.value.rightchild)
#
#
# def searchBST(rootNode,nodeValue):
#     if not rootNode:
#         return
#     else:
#         customQueue  = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not customQueue.isEmpty():
#             root = customQueue.dequeue()
#             if root.value.data == nodeValue:
#                 return 'success'
#             if (root.value.leftchild is not None):
#                 customQueue.enqueue(root.value.leftchild)
#             if (root.value.rightchild is not None):
#                 customQueue.enqueue(root.value.rightchild)
#         return 'not found'
#
#
# def insertNode(rootNode,newNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not customQueue.isEmpty():
#             root = customQueue.dequeue()
#             if root.value.leftchild is not None:
#                 customQueue.enqueue(root.value.leftchild)
#             else:
#                 root.value.leftchild = newNode
#                 return 'succesfully inserted'
#             if root.value.rightchild is not None:
#                 customQueue.enqueue(root.value.rightchild)
#             else:
#                 root.value.rightchild = newNode
#                 return 'succussfully inserted'
#
# # newNode = TreeNode('colddrink')
# # print(insertNode(newBT,newNode))
# # levelOrderTraversal(newBT)
#
# def getDeepestNode(rootNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not customQueue.isEmpty():
#             root = customQueue.dequeue()
#             if root.value.leftchild is not None:
#                 customQueue.enqueue(root.value.leftchild)
#             if root.value.rightchild is not None:
#                 customQueue.enqueue(root.value.rightchild)
#         deepestNode = root.value
#         return deepestNode
#
# # deepestNode = getDeepestNode(newBT)
# def deleteDeepesNode(rootNode,dNode):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not customQueue.isEmpty():
#             root = customQueue.dequeue()
#             if root.value is dNode:
#                 root.value = None
#             return
#             if root.value.rightchild:
#                 if root.value.rightchild is dNode:
#                     root.value.rightchild = None
#                     return
#                 else:
#                     customQueue.enqueue(root.value.rightchild)
#             if root.value.leftchild:
#                 if root.value.leftchild is dNode:
#                     root.value.leftchild = None
#                     return
#                 else:
#                     customQueue.enqueue(root.value.leftchild)
#
# def deleteNodeBT(rootNode,node):
#     if not rootNode:
#         return
#     else:
#         customQueue = queue.Queue()
#         customQueue.enqueue(rootNode)
#         while not customQueue.isEmpty():
#             root = customQueue.dequeue()
#             if root.value.data == node:
#                 dNode = getDeepestNode(rootNode)
#                 root.value.data = dNode.data
#                 deleteDeepesNode(rootNode,dNode)
#                 return 'the node has been successfully deleted'
#             if root.value.leftchild is not None:
#                 customQueue.enqueue(root.value.leftchild)
#             if root.value.rightchild is not None:
#                 customQueue.enqueue(root.value.rightchild)
#         return 'failed to delete'
#
# def deleteall(rootNode):
#     rootNode.data= None
#     rootNode.leftchild = None
#     rootNode.rightchild = None
#     return 'all have been deleted successfully'
#
# deleteall(newBT)
# levelOrderTraversal(newBT)
