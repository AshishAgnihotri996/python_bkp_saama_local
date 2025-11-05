Given a list of numbers, write a Python program to find the sum of all the elements in the list.
l =[2,3,5,6,4]
i = 0
j = l[-1]
ans = 0

for i in range(i,j+1):
    ans+=l[i]
print(ans)

2nd cumulative
l = [2,4,5,6,3,5,6]
i = 1
j = 3

for x in range(len(l)):
     if (i==0):
         continue
     else:
         l[x]=l[x]+l[x-1]

if(i==0):
    print(l[i])
else:
    print(l[j]-l[i-1])


l=[3,43,653,34,67,34]
s =1
e =5
print(sum(l[s:e+1]))

Python Program to Square Each Odd Number in a List using List Comprehension

l = [1,2,3,4,65,7,8]
x = [i*i for i in l ]
print(x)

Python – Get the object with the max attribute value in a list of objects

from operator import attrgetter

class abc:
    def __init__(self,exp,sal):
        self.exp = exp
        self.sal = sal

obj1 = abc(2,3000)
obj2 = abc(4,4000)
obj3 = abc(6,5000)
obj4 = abc(7,6000)
obj5 = abc(8,8000)

l = [obj4,obj5,obj2,obj1,obj3]
max_attr = max(l,key=attrgetter('exp'))
print(max_attr.exp)


remove common element from the list


out =[]

def remove_commom(a,b):
    # for i in a[:]:
    #     if i in b:
    #         a.remove(i)
    #         b.remove(i)
    # a,b =[i for i in a if a not in b],[j for j in b if j not in b]
    # a,b = list(set(a) - set(b)),list(set(b)- set(a))
    print(a)
    print(b)

a = [1,2,3,4,6]
b = [4,5,6,7,8]

remove_commom(a,b)

Python – Get the indices of all occurrences of an element in a list

my_list = [1, 2, 3, 1, 5, 4]
new_list = len(my_list)
for i in range(new_list):
    if (my_list[i]==1):
        print(i)

a= [1,5,3,2,5,3]
item =5
x = [i for i in range(len(a)) if a[i]==item ]
print(x)

list1 = ['sravan', 98, 'harsha', 'jyothika',
         'deepika', 78, 90, 'ramya']
list1
# for i in list1:
#     if type(i)==str:
#         print(list1.index(i))

print([list.index(i) for i in list1 if (type(i)is str)])
print([i for i in list1 if(type(i)is str)])

Convert list of dictionaries to dictionary of lists

data = [
    {'name': 'sravan', 'subjects': ['java', 'python']},
    {'name': 'bobby', 'subjects': ['c/cpp', 'java']},
    {'name': 'ojsawi', 'subjects': ['iot', 'cloud']},
    {'name': 'rohith', 'subjects': ['php', 'os']},
    {'name': 'gnanesh', 'subjects': ['html', 'sql']}

]

dict_of_lsit ={}

for item in data:
    name = item['name']
    dict_of_lsit[name] = item

print(dict_of_lsit)

program to convert a byte string to a list of integers
s = "ashish is a good boy"

out =[]

for char in s:
    out.append(ord(char))

print(out)

matrix

test_list1 = [[4, 3, 5, ], [1, 2, 3], [3, 7, 4]]
test_list2 = [[1, 3], [9, 3, 5, 7], [8]]

print("The original list 1 is : " + str(test_list1))
print("The original list 2 is : " + str(test_list2))

for i,j in enumerate(test_list1):
    new_val =[]
    for j in test_list2:
        new_val.append(i)
    test_list1[i].extend(new_val)

or

x = [sub1+sub2 for sub1, sub2 in zip(test_list1,test_list2)]

print("The concatenated Matrix : " + str(x))

binary search tree

creat a binary serach tree

class BST:
    def __init__(self,data):
        self.data= data
        self.leftChild =None
        self.rightChild = None

def insertNode(rootNode,nodeValue):
    if rootNode.data is None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BST(nodeValue)
        else:
            insertNode(rootNode.leftChild,nodeValue)
    else:
        if nodeValue >= rootNode.data:
            if rootNode.rightChild is None:
                rootNode.rightChild = BST(nodeValue)
        else:
            insertNode(rootNode.rightChild,nodeValue)
    return 'succussfully'

def searchNode(rootNode,nodeValue):
    if rootNode.data == nodeValue:
        print('the value is found')
    elif nodeValue < rootNode.data:
        if rootNode.leftChild == nodeValue:
            print('the value is found')
        else:
            searchNode(rootNode.leftChild,nodeValue)
    else:
        if rootNode.rightChild == nodeValue:
            print('the value is found')
        else:
            searchNode(rootNode.rightChild,nodeValue)

def minValueNode(bstNode):
    current = bstNode
    while(current.leftChild is not None):
        current = current.leftChild
    return current


def deleteNode(rootNode,nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(rootNode.leftChild,nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(rootNode.rightChild,nodeValue)

    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = minValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = deleteNode(rootNode.rightChild,temp.data)
    return rootNode

newBst = BST(None)
print(insertNode(newBst,60))
print(insertNode(newBst,50))
print(insertNode(newBst,40))
print(insertNode(newBst,20))
print(insertNode(newBst,20))
print(insertNode(newBst,10))
print(insertNode(newBst,70))
print(newBst.data)
print(newBst.leftChild.data)
print(searchNode(newBst,40))
print(deleteNode(newBst,40))
print(newBst.data)

binary search
import math


def binarySearch(array,value):
    start = 0
    end = len(array)-1
    middle = math.floor((start+end)/2)

    while not(array[middle]==value) and start <= end:
        if value < array[middle]:
            end = middle -1
        else:
                start = middle +1
        middle = math.floor((start + end) / 2)
    if array[middle] == value:
        return middle
    else:
        return  -1


array = [1,2,4,5,6,7,8,9,10,12,14,16]
print(binarySearch(array,5))
import string
def outer(function):
    def inner(first,last):
        first = str.upper(first)
        last = str.upper(last)
        ot = first+' '+last
        print(ot)
        # return ot
    return inner

def cap(function):
    def inner(first,last):
        first = str.capitalize(first)
        last = str.capitalize(last)
        otp = first+' '+last
        print(otp)
    return inner

@outer
@cap
def names(first,last):
    print(first+' '+last)

names('ashish','agnihotri')





# def isBalanced(expr):
#     stack =[]
#
#     for char in expr:
#         if char in ["[","{","("]:
#             stack.append(char)
#         else:
#             if not stack:
#                 return False
#             current_char = stack.pop()
#             if current_char == '(':
#                 if char!= ')':
#                     return False
#             if current_char == '{':
#                 if char!= '}':
#                     return False
#             if current_char == '[':
#                 if char!= ']':
#                     return False
#     if stack:
#         print('ok')
#     else:
#         print('not')
# expr ='[]'
# isBalanced(expr)
