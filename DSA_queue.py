# #queue without size limit
# #
# class Queue:
#     def __init__(self):
#         self.list = []
#
#     def __str__(self):
#         values = [str(x) for x in self.list]
#         return ' \n'.join(values)
#
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False
#
#     def enqueue(self,values):
#         self.list.append(values)
#         return 'the element has been success fully inserted'
#
#     def dequeue(self):
#         if self.isEmpty():
#             return True
#         else:
#             return self.i.pop(0)
#
#     def peek(self):
#         if self.isEmpty():
#             return 'no element in the queue'
#         else:
#             return self.list[0]
#
#     def deletemeth(self):
#         self.list = None
#         return 'deleted no eleent found'
#
# customqueue = Queue()
# customqueue.enqueue(1)
# customqueue.enqueue(2)
# customqueue.enqueue(3)
# customqueue.enqueue(4)
# print(customqueue)

#queue linked list
#
# class Queue:
#     def __init__(self,maxsize):
#         self.items = maxsize *[None]
#         self.maxsize = maxsize
#         self.start = -1
#         self.top = -1
#
#     def __str__(self):
#         values = [str(x) for x in self.items]
#         return ' '.join(values)
#
#     def isFulll(self):
#         if self.top + 1 ==self.start:
#             return True
#         elif self.start ==0 and self.top + 1 == self.maxsize:
#             return True
#         else:
#             return False
#     def isEmpty(self):
#         if self.top ==-1:
#             return True
#         else:
#             return False
#     def enqueue(self,value):
#         if self.isFulll():
#             return 'the queue is Empty'
#         else:
#             if self.top + 1 ==self.maxsize:
#                 self.top = 0
#             else:
#                 self.top +=1
#                 if self.start == -1:
#                     self.start = 0
#             self.items[self.top] = value
#             return  'the element has been inserted at the end of the queue'
#
#     def dequeue(self):
#         if self.isEmpty():
#             return 'there are not any element'
#         else:
#             firstelement = self.items[self.start]
#             start = self.start
#             if self.start == self.top:
#                 self.start = -1
#                 self.top =-2
#             elif self.start +1 == self.maxsize:
#                 self.start = 0
#             else:
#                 self.start +=1
#             self.items [start] = None
#             return firstelement
#
#     def delete(self):
#         self.list = None
#         return 'deleted no eleent found'
#
# customequeue = Queue(3)
# customequeue.enqueue(1)
# customequeue.enqueue(2)
# customequeue.enqueue(3)
# print(customequeue)


#-----------------------------------------------------------------------------------------------------------------------
# class Queue:
#     def __init__(self):
#        self.items = []
#
#     def __str__(self):
#         value = [str[x] for x in self.items]
#         return ' '.join(value)
#
#     def isEmpty(self):
#         if self.items == []:
#             return True
#         else:
#             return False
#
#     def enqueue(self,value):
#         self.items.append(value)
#         return 'inserted successfully'
#
#     def dequeue(self):
#         if self.isEmpty():
#             return 'no element in the queue'
#         else:
#             return self.items.pop(0)
#     def peek(self):
#         if self.isEmpty():
#             return 'no element'
#         else:
#             return self.items[0]
#
#     def delete(self):
#         self.items = None
#         return 'element deleted'
#
# customQueue = Queue()
# customQueue.enqueue(1)
# customQueue.enqueue(2)
# customQueue.enqueue(3)
# customQueue.delete()
# print(customQueue)


#------------------ queue with capacity---

class Queue:
    def __init__(self,maxSize):
        self.maxSize = maxSize
        self.items = maxSize * [None]
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.top +1 == self.start:
            return True
        elif self.start == 0 and self.top +1 == self.maxSize:
            return True
        else:
            return False

    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return False

    def enqueue(self,value):
        if self.isFull():
            return 'not foiund'
        else:
            if self.top + 1 ==self.maxSize:
                self.top = 0
            else:
                self.top +=1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return  'the element is inserted in the end of the queue'

    def dequeue(self):
        if self.isEmpty():
            return 'no element'
        else:
            firstElement = self.start
            if self.start == self.top:
                self.top = -1
                self.start = -1
            elif self.start +1 == self.maxSize:
                self.start =0
            else:
                self.start +=1
            self.items[self.start] = None
            return firstElement

    def peek(self):
        if self.isFull():
            return 'no element'
        else:
            self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1

customQueue = Queue(3)
customQueue.enqueue(1)
customQueue.enqueue(2)
customQueue.enqueue(3)
# customQueue.delete()
print(customQueue)