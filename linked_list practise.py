# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.head = None
#         self.next = None
#
# #create linked list
# class Linkedlist:
#     def printedlist(self):
#         pointer = self.head
#         linked_list = ""
#         while(pointer):
#             linked_list+=(str(pointer.data)+" ")
#             pointer = pointer.next
#         print(linked_list)
#
# # insert linkedlist
#
#     def insertnode(self,val,pos):
#         target = Node(val)
#         if (pos ==0):
#             target.next = self.head
#             self.head = target
#             return
#
#         def getprev(pos):
#             temp = self.head
#             count = 1
#             while(count < pos):
#                 temp=temp.next
#                 count+=1
#             return temp
#
#         prev=getprev(pos)
#         newNode = prev.next
#
#         prev.next = target
#         target.next = newNode
#
#     # def deletenode(self,key):
#     #     temp = self.head
#     #     if(temp is None):
#     #         return
#     #     if(temp.data == key):
#     #         self.head=temp.next
#     #         temp = None
#     #         return
#     #     while(temp.next.data != key):
#     #         temp = temp.next
#     #
#     #     target_node = temp.next
#     #     temp.next=target_node.next
#     #     target_node.next = None
#
#
# linked_list = Linkedlist()
# linked_list.head = Node(5)
# second_node = Node(3)
# third_node = Node(1)
# fourth_node = Node(7)
#
# linked_list.head.next = second_node
# second_node.next = third_node
# third_node.next = fourth_node
# linked_list.printedlist()
#
# linked_list.insertnode(2,2)
# linked_list.printedlist()

# linked_list.deletenode(3)
# linked_list.printedlist()
#
#

#doubly linked list

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.prev = None
#         self.next = None
# class DoublyLinkedList:
#     def createlist(self,arr):
#         self.head = None
#         start = self.head
#         n = len(arr)
#         temp  =start
#         i= 0
#         while(i<n):
#             newNode=Node(arr[i])
#             if (i==0):
#                 start = newNode
#                 temp = start
#             else:
#                 temp.next=newNode
#                 newNode.prev = temp
#                 temp = temp.next
#             i+=1
#         self.head = start
#         return start
#     def printlinkedlist(self):
#         temp = self.head
#         linked_list = ""
#         while(temp):
#             linked_list+=(str(temp.data)+" ")
#             temp = temp.next
#         print(linked_list)
#
#     def countList(self):
#         temp = self.head
#         count = 0
#         while(temp is not None):
#             temp = temp.next
#         count+=1
#         return count
#
#     def insertAtLocation(self,value ,index):
#         temp = self.head
#         count = self.countList()
#         if(count+1<index):
#             return temp
#         newNode = Node(value)
#
#         if (index ==1):
#             newNode.next = temp
#             temp.prev = newNode
#             self.head = newNode
#             return self.head
#         if(index == count+1):
#             while(temp.next is not None):
#                 temp= temp.next
#
#             temp.next = newNode
#             newNode.prev = temp
#             return self.head
#
#         i=1
#         while(i<index-1):
#             temp = temp.next
#             i+=1
#
#         nodeAtTarget = temp.next
#         newNode.next = nodeAtTarget
#         nodeAtTarget.prev = newNode
#
#         temp.next = newNode
#         newNode.prev = temp
#
#         return self.head
#
#
#
# arr =[1,2,3,4,5]
# list = DoublyLinkedList()
# list.createlist(arr)
# list.printlinkedlist()
#
# list.insertAtLocation(8,5)
# list.printlinkedlist()

#merge 2 linked list
# class ListNode:
#     def __init__(self,x):
#         self.val = x
#         self.next = None
#
# class solution:
#     def mergeTwoLinkedList(self,l1:ListNode,l2:ListNode):
#         cur = ListNode(0)
#         ans = cur
#
#         while(l1 and l2):
#             if l1.val > l2.val:
#                 curr.next=l2
#                 l2 = l1.next
#             else:
#                 cur.next = l1
#                 l1 = l2.next
#
#             cur = cur.next
#
#             while(l1_1):
#                 cur.next = l1
#                 l1 = l1.next
#                 cur = cur.next
#
#             while(l2_1):
#                 cur.next = l2
#                 l2 = l2.next
#                 cur = cur.next
#
#             return ans.next
#
# s = solution()
# l1_1 = ListNode(1)
# l1_2 = ListNode(2)
# l1_4 = ListNode(3)
#
# l1_1.next = l1_2
# l1_2.next = l1_4
#
# l2_1 = ListNode(2)
# l2_2 = ListNode(1)
# l2_3= ListNode(4)
#
# l2_1.next = l2_2
# l2_2.next = l2_3
#
# ans = s.mergeTwoLinkedList(l1_1,l2_1)
# print(ans)
#
# while(ans!=None):
#     print(ans.val)
#     ans= ans.next
#

#cycle problem

# class Solution:
#     def cycle(self,head:listNode):
#         hare = head
#         turtle = head
#
#         while turtle and hare and hare.next:
#             hare = hare.next.next
#             turtle = not turtle
#             if (turtle == hare):
#                 return True
#         return False
#
# listNode=
# s = Solution()
# s.cycle()

#circular linked list

# class Node:
#     def __init__(self,data):
#         self.data = data
#         self.next = None
#
# class Solution:
#     def reverseLinkedlist(self,head:Node):
#         node = None
#         while(node is not None):
#             next = head.next
#             head.next = node
#             node = head
#             head = next
#         return node
# s = Solution()
#
# l1 = Node(1)
# l2 = Node(2)
# l3 = Node(3)
# l4 = Node(4)
# l5 = Node(5)
#
# l1.next = l2
# l2.next =l3
# l3.next = l4
# l4.next = l5
#
# ans = s.reverseLinkedlist(l1)
# print(ans.data)

#add two numbers


#delte form the n element

class Node:
    def __init__(self,val):
        self.val = val
        self.next = None

class Solution:
    def deletefromthenelement(self,head:Node,n):
        ans = Node(0)
        ans.next = head

        first = ans
        second = ans

        for i in range(1,n+2):
            first = first.next

        while(first is not None):
            first = first.next
            second = second.next

        second.next = second.next.next

        return ans.next

s = Solution()

l1 = Node(1)
l2 = Node(2)
l3 = Node(3)

l1.next = l2
l2.next = l3

ans = s.deletefromthenelement(l1,2)

while(ans != None):
    print(ans.val)
    ans = ans.next