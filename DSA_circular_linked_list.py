#cration of a CIRCULAR LINKED LIST
class Node:
    def __init__(self,value):
        self.value = value
        self.next  = None

class CLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def CreateCLL(self,nodeValue):
        node= Node(nodeValue)
        node.next = node
        self.head= node
        self.tail = node


#insertion into circular dLL
    def insertDCLL(self,value,location):
        if self.head is None:
            return 'false'
        else:
            newNode = Node(value)
            if location ==0:
                newNode.next  = self.head
                self.head = newNode
                self.tail.next = newNode

            elif location ==1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode

            else:
                tempnode = self.head
                index = 0
                while index < location -1:
                    tempnode = tempnode.next
                    index+=1
                nextnode = tempnode.next
                tempnode.next = newNode
                newNode.next = nextnode

    def traversal(self):
        if self.head is None:
            print('not found')
        else:
            temp = self.head
            while temp:
                print(temp.value)
                temp = temp.next
                if temp == self.tail.next:
                    break

    def searchNode(self,nodevalue):
        if self.head is None:
            print('no node exist')
        else:
            temp = self.head
            while temp:
                if nodevalue == temp.value:
                    return nodevalue
                temp = temp.next
                if temp == self.tail.next:
                    break



#deletion

    def deletenode(self,location):
        if self.head is None:
            return -1
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.tail.next = self.head

            elif location ==1:
                if self.head == self.tail:
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    node = self.head
                    while node is not None:
                        if node.next == self.tail:
                            break
                        node = node.next
                    node.next = self.head
                    sefl.tail = node
            else:
                tempnode = self.head
                index = 0
                while index < location -1:
                    tempnode = tempnode.next
                    index +=1
                nextnode = tempnode.next
                tempnode.next = nextnode.next


    def deleteentirelist(self):
        self.head = None
        self.tail.next  = None
        self.tail = None


SS = CLinkedList()
SS.CreateCLL(1)
SS.insertDCLL(1,2)
SS.insertDCLL(2,2)
SS.insertDCLL(3,3)
SS.insertDCLL(4,4)
SS.insertDCLL(5,5)

print([node.value for node in SS])
# SS.traversal()
#SS.deletenode(2)
SS.deleteentirelist()
print(node.value for node in SS)
