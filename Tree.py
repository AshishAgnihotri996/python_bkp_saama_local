# class Node:
#     def __init__(self,val):
#         self.left = None
#         self.right = None
#         self.val = val
#
# def postorder(node):
#     if (Node is not None):
#         postorder(node.left)
#         postorder(node.right)
#         print(node.val)
#
# #create node
# root = Node(4)
# root.left = Node(5)
# root.right = Node(6)
# root.left.left = Node(7)
# postorder(root)

#create a binary tree and insert some data
#
# class Node:
#     def __init__(self,val):
#         self.left = None
#         self.right= None
#         self.data = val
#
# def insert(root,node):
#     if (root is None):
#         root = node
#         return
#     if (root.data < node.data):
#         if (root.right is None):
#             root.right = node
#         else:
#             insert(root.right,node)
#     else:
#         if (root.left is None):
#             root.left = node
#         else:
#             insert(root.left,node)
#
# def preorder(node):
#     if node is not None:
#         print(node.data)
#         preorder(node.left)
#         preorder(node.right)
#
#
# tree= Node(5)
# insert(tree,Node(5))
# insert(tree,Node(3))
# insert(tree,Node(2))
# insert(tree,Node(4))
# insert(tree,Node(7))
# insert(tree,Node(6))
# insert(tree,Node(8))
#
# preorder(tree)
#
# class Solution:
#     def maxsubstree(self,root:Treenode)->int:
#         if root is None:
#             return 0
#         if root is leafnode:
#             return 1
#
#         left = self.maxsubtree(root.left)
#         right = self.maxsubtree(root.right)
#         return max(left,right)+1

# class Solution:
#     def hasSum(self,root,sum,cur):
#         if root is None:
#             return False
#         curr+=root.value
#         if (curr== sum):
#             return True
#         return (self.hasSum(rot.left,sum,curr) or self.hasSum(root.right,sum,curr))
#
#     def hasPathsum(self,root:Treenode)->bool:
#         return self.hasSum(root,sum,0)


#fkth smallest element is bst

class Solution:
    def kthsmalles(self,root:treenode,k)->int:
        self.k = k
        self.res = None
        self.inorder(root)
        return self.res

    def inorder(self,root):
        if not root:
            return
        self.inorder(root.left)
        k -=1
        if self.k==0:
            self.res = root.val
            return
        self.inorder(root.right)