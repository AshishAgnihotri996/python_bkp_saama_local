# # ----------- with list-----------
# class stack:
#     def __init__(self):
#         self.list = []
#
#     def __str__(self):
#         values = self.list.reverse()
#         values = [str(x) for x in self.list]
#         return '\n'.join(values)
#
#     def isEmpty(self):
#         if self.list == []:
#             return True
#         else:
#             return False
#
#     def push(self,values):
#         self.list.append(values)
#         return 'values has been inserted successfully'
#
#     def pop(self):
#         if self.isEmpty():
#             return 'no element in the stack'
#         else:
#             return self.list.pop()
#
#     def peek(self):
#         if self.isEmpty():
#             return 'there is not any element is the stack'
#         else:
#             return  self.list[len(self.list)-1]
#
#     def delete_lst(self):
#         self.list = None
#
#
# customestack = stack()
# # customestack.pop(1)
# customestack.push(1)
# customestack.push(2)
# customestack.push(3)
# customestack.push(4)
# customestack.push(5)
# # customestack.pop()
#
# print(customestack.delete_lst())


#------------stack with size limit-------------
class stack:
    def __init__(self):
        self.list= []
    def __str__(self):
        values = self.list.reverse()
        values = [str(x)for x in self.list]
        return ' \n '.join(values)

    #isempty
    def isempty(self):
        if self.list == []:
            return True
        else:
            return False

    #push
    def pushmeth(self,value):
        self.list.append(value)
        return 'element is been inserted successfully'

    #pop
    def popeth(self):
        if self.list == []:
            return 'not found'
        else:
            self.list.pop()

    def peek(self):
        if self.isempty():
            return 'empty'
        else:
            return self.list(len(self.list)-1)


customStack = stack()
customStack.pushmeth(1)
customStack.pushmeth(2)
customStack.pushmeth(3)
customStack.pushmeth(4)
customStack.pushmeth(5)
print(customStack.peek())

