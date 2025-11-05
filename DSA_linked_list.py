# singly linkedlist creation
# class Node:
#     def __init__(self,value):
#         self.data = value
#         self.next = Null
#
# class Linked_list:
#     def __init__(self):
#         self.head = Null
#         self.tail = Null
#
# ll = Linked_list()
# node1 = Node(1)
# node2= Node(2)
#
# ll.head = node1
# ll.head.next = node2
# ll.tail = node2

#insertation in a linked list

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Singly_LinkedList:
    def __init__(self):
        self.head = None
        self.tail  =None

    # to print the linked list
    def __iter__(self):
        node = self.head
        while node:
            yield node
        node = node.next

# insert into  a linked list

    def insertLinkedList(self,value,location):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:
               newNode.next = self.head
               self.head = newNode
            elif location == 1:
                newNode.next = None
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempnode = self.head
                index = 0
                while index < location-1:
                    tempnode = tempnode.next
                    index+=1
                    nextnode = tempnode.next
                    tempnode.next = newNode
                    newNode.next = nextnode

    def traversal(self):
        if self.head is None:
            print('nthg found')
        else:
            node = self.head
            while node is not None:
                print(node.value)
                node = node.next

    def searchfun(self,nodevalue):
        if self.head is None:
            print('nothng found')
        else:
            node = self.head
            while node is not None:
                if node.value==nodevalue:
                    return node.value
                node = node.next
        return 'not found'

#---------delete a node in the linked list


    def deletelinkesList(self,location):
        if self.head is None:
            return False

        elif location == 0:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node is not None:
                    if node.next == self.tail:
                        break
                    node = node.next
                    self.tail = node

        else:
            tempnode = self.head
            index = 0
            while index < location-1:
                tempnode = tempnode.next
                index +=1
            nextnode = tempnode.next
            tempnode.next = nextnode.next

#delete entire linked list
    def deleteentirelinkedlist(self):
        if self.head is None:
            print('not found')
        else:
            self.head= None
            self.tial = None



singlylinkedlist = Singly_LinkedList()
singlylinkedlist.insertLinkedList(1,1)
singlylinkedlist.insertLinkedList(2,1)
singlylinkedlist.insertLinkedList(3,1)
singlylinkedlist.insertLinkedList(4,1)
#print([node.value for node in singlylinkedlist])
#singlylinkedlist.traversal()
print(singlylinkedlist.searchfun(3))
print(singlylinkedlist.deletelinkesList(2))
singlylinkedlist.deleteentirelinkedlist()
print([node.value for node in singlylinkedlist])


