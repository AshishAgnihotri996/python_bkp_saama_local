#creation of a double linked list

class Node:
    def __init__(self,value):
        self.value = value
        self.prev = None
        self.next = None

class Double_linked_list:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
        node = node.next

    def creationDLL(self,nodevalue):
        node = Node(nodevalue)
        self.prev = None
        self.next = None
        self.head = node
        self.tail = node
        return 'the DLL been created successfullt'


#insertion method in DLL
    def insertMethod(self,nodevalue,location):
        if self.head is None:
            return -1
        else:
            newNode = Node(nodevalue)
            if location == 0:
                newNode.next = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location ==1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail= newNode
            else:
                tempnode = self.head
                index = 0
                while index < location -1:
                    tempnode = tempnode.next
                    index+=1
                newnode.next = tempnode.next
                newNode.prev = tempnode
                newNode.next.prev = newNode
                tempnode.next = newNode


#traversal

    def traversal(self):
        if self.head is None:
            return -1
        else:
            tempnode = self.head
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.next
#reverse travseral
    def reverseTraversal(self):
        if self.head is None:
            return -1
        else:
            tempnode = self.tail
            while tempnode:
                print(tempnode.value)
                tempnode = tempnode.prev

#searching
    def search(self,nodevalue):
        if self.head is None:
            return 'not found'
        else:
            tempnode = self.head
            while tempnode:
                if tempnode.value == nodevalue:
                    print(tempnode.value)
                    tempnode = tempnode.next

            return 'node does not exist'

#delete

    def deleteDLL(self,location):
        if self.head is None:
            print('not fouind')
        else:
            if location == 0
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = None
            elif location == 1:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = None
            else:
                tempnode = self.head
                index = 0
                while index < location - 1:
                    tempnode = tempnode.next
                    index +=1
                    tempnode.next = tempnode.next.next
                    tempnode.next.prev = tempnode

    def deleteEntireList(self):
        if self.head is None:
            print('there is no node')
        else:
            tempnode = self.head
            while tempnode:
                tempnode.prev = None
                tempnode = tempnode.next
            self.head = None
            self.tail = None
            print('all node has been deelete')


DLL = Double_linked_list()

DLL.insertMethod(0,0)
DLL.insertMethod(2,1)
print([node.value for node in DLL])
DLL.deleteDLL(3)