#
#
#
# 6.
#
#
# def fun():
#     print('Hello world')
#
#
# fun() - Its
# not a
# function.Its
# a
# reference
# variable
# type(fun()) - NoneType
# type(fun) - Function
#
# 7.
# Python
# uses
# interpreter or compiler?
# Ans.: It
# uses
# both.Its
# of
# a
# Hybrid
# type
#
# RAM
# contains
# two
# parts - Heap and Stack
# In
# Python, everything
# gets
# stored
# on
# Heap
# memory
# inside
# RAM and not in stack.
# Because in python
# everything is a
# object.
#
# Example:
#
#
# class One:
#     def show():
#         print('Hello World')
#         num = 100
#
#
# o = One()
# o.show()
#
# Here
# 'show' is a
# method and 'print' is a
# function.
#
#
# num5 = 500
# num6 = 500
#
# print(id(num5))
# print(id(num6))
# #same value
#
#
# num7 = 25
# num8 = 25
#
# print(id(num7))
# print(id(num8))
# #same value
#
# '''
#
# n1 = 3.14
# n2 = 3.14
#
# print(id(n1))
# print(id(n2))
# # same value on IDLE
# # different ID on Shell
#
# '''
# Whatever we do on shell it will load from memory only single time.
# On IDLE, it stores in a memory, so we get the same addr every time.
# '''
#
#
# ----------------------3------------
#
# # empty dictionary
# dict1 = {}
# print(dict1)
# print(type(dict1))  # dictionary
#
# # empty set
# set1 = {}
# print(set1)
# print(type(set1))   # dictionary
#
# # String as key and value as int
# dict2 = {'A' : 100}
# print(dict2)    # Possible
#
# # float as key and value as int
# dict3 = {3.14 : 100}
# print(dict3)    # Possible
#
# # list as key and int as value
# # dict4 = {[1, 2, 3] : 100}
# # print(dict4)    # not possible
# # TypeError: Unhashable type: 'list'
# # unhashable means changeable
#
# # Tuple as key and int as value
# dict5 = {(1, 2, 3) : 100}
# print(dict5)        # possible
#
# print(dict5.get((1, 2, 3))) # we need to pass whole tuple to get the value
#
#
# # key as int and value as list
# dict6 = {10 : [1, 2, 3, 4]}
# print(dict6)
# print(dict6[10][2])
#
#
# # Sub Dictionaries - Dictionary inside dictionary
# subdict = { 'key1': {1: 'value1', 2: 'value2'}, 'key2': {3: 'value3', 4: 'value4'} }
# print(subdict)
# print(subdict.keys())       # It will return keys in form of list
# print(subdict.values())     # It will return values in form of list
#
#
# # dictionary as key and string as value
# dict7 = {{1: 10, 2: 20}: 'ABCD'}
# print(dict7)  # Not possible
# # TypeError: unhashable type: 'dict'
#
# list1 = [1, 2, 3, 4, 5]
#
# print(list1.append(99))     # None
# # The statement should be like this
# # list1.append(99)
#
# print(list1)
#
# #list1.extend(100)   # It will give type error that int can not be iterable
# list1.extend([100])
# print(list1)
#
# # index, value
# list1.insert(7, 101)
# print(list1)
#
#
# # print(1 + 'Hi')
# # TypeError: unsupported operand type(s) for +: 'int' and 'str'
#
# #print(1 + 1.2)
#
# # Copying one list into another
# list1 = (1, 2, 3)
# list2 = list1   # Both lists have same id. So changes in one list impact the other list also
# # Such copy is known as Shallow Copy
# print(list1)
# print(list2)
#
# list3 = (1, 2, 3)
# list4 = list3.copy()
# # For this both lists have different id so it will not impact on each other
#
# print(list3)
# print(list4)
#
# '''
# # list5 = (4, 5, 6)
# # list6 = (7, 8, 9)
# # list7 = list5 + list6   # here '+' operator is used as concatenation
# # # we can not add 2 lists
# # print(list7)
#
#
# #day--
#
# tup = ()
# print(tup)
#
# tup2 = (1,'ashish','agnihotri',3.14)
# print(tup2)

#remove redundant paranthesis
# tupex = ("asg",)
# print(type(tupex))

# 2 methods

# tu = (1,2,2,3,4,5)
# print(tu.count(2))
#
# print(tu.index(2))
#
# del tu
# print(tu)

# tu10 = (1,2,3)
# tu11 = ('ashish','agnihotri')
# print(tu10+tu11)


# de structing
#unpacking

# x,y = "hii",7
# print(x)
# print(y)


#---------------senario------

#list inside tuple
# tupp = (1,2,3,[1,2,3])
# print(tupp)
# del tupp[3][0]
# print(tupp)


# tuple inside list
# tupp1 = [1,2,3,(1,2,3)]
# print(tupp1)
# del tupp1[-1]
# print(tupp1)

#------type casting----
# tu = [1,2,34,5]
# li = tuple(tu)
# print(type(li))

# tu = (1,2,3,4,{1:'true'})
# print(type(tu))


#for loop ---> comprehensions

# obj = [("Even",i) if i%2==0 else "odd" for i  in range(20)]
# print(obj)



#why tuple is faster than list

# import os
#
# li = [1,2,3,4,5,6]
# print(li.__sizeof__())
#
# tup = (1,2,3,4,5,6,7)
# print(tup.__sizeof__())
#
# from timeit import timeit
#
# start = timeit
# listdemo = [1,2,3,4,5,6,7]
# end = timeit
# x = (end-start)
# print(listdemo,x)
#
# #ref var --> adress of that particular object
#
# #chaining
# list1 = [1,2,3,[4,5]]
# list1.append(3)
# print(list1)

#keys can be immurtable entity and mutuable entites ar enot possible

#access part
# print(dic2['lang'])
# print(dic5[10,20])
#
# #update count of pairs of dictionary
# dict.update({22:300})
# print(dict)


# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
# print("dict['Name']: ", dict['Name'])
# print("dict['Age']: ", dict['Age'])


#string
# ord() and char()
# print(ord('a'))
# print(chr(923))

#indexing and slicing
#start --0, stop = end-1, step -> optional/ increment

# a ='ashish agnihotri'
# print(a[6:10])
# print(a[-1:0:1])
# print(a[:4])
# print(a[::])
# print(a[0::3])
# print(a[-1:-10:-1])
# print(a[-1:-10:-2])
# print(a[-1:-10:1])
# print(a[-1::-1])
# print(a[-1:-1:-1])
# print(a[3:12:2])
# print(a[4:3:-2])
# print(a[:-4:-1])
# print(a[:-4:-1])
# print(a[:-4:-1])
# print(a[0:0])
# print(a[-1:5:-3])

#concatenation - to add 2 or more strings

# count the length of the string

# def countofchar(a):
#     counter = 0
#     for i in a:
#         counter+=1
#     print(counter)
# a='ashish agnihotri'
# countofchar(a)

#vowels

# def vowels(str1):
#     counter = 0
#     aa = ['a','e','i','o','u']
#     for char in str1:
#         if char in aa:
#             counter+=1
#     print(counter)
#
# str1 = 'ashish agnihotri'
# vowels(str1)

#no of occurance

# aa = 'ashish agnihotri'
# c = aa.count('i')
# # c = aa.count('i',1,10) --> start and end is optional
# print(c)


#enumarate to check the index and element

# aa ='ashish agnihotri'
# print(enumerate(aa))

# find, rfing, index, rindex

# startwith/ endwith

# aa = 'ashish agnihotri'
# if aa.endswith('ashish'):
#     print('found it')
# else:
#     print('not found')


# replace method

# str1 = 'hello world'
# print(str1.replace('hello','yo'))

#comparision operator
# name = 'ashish'
# name1= 'ashishe'
# print(name==name1)

# lstrip , rstrip

# name=input('enter the name')
# name = name.lstrip()
# print(name)

# url = 'https://www.google.com'
# for i in url:
#     x = url.lstrip('htps/:w.')
# print(x)

#strip - removes leading and trailing char
#if mismatch then it doest remove , just shows as it is..

#string formatting
# c style formatting
# .foramt() classmethod
# f-string

# name = input('enter the name')
# age = int(input('enter thr age'))
# print(f'the name is {name} and age is {age}')

#reverse a string
# while loop
# name = input('enter the name')
# print('original string ',name)
# r_name = ""
# count = len(name)
# while count > 0 :
#     r_name=r_name+name[count-1]
#     count-= 1
# print(r_name)

#using for loop
# name = input('enter the name')
# print('original string ',name)
# r_name = ""
# count = len(name)
#
# for char in name:
#     r_name = char+r_name
# print(r_name)

#using slicing
# name = 'ashish'
# print(name[::-1])

#-----------------------------------------------OOPS----------------------------------------
import sys

# index 2 types - > positive and negative
#
# immutabe - > int, float, string, tuple
#
# 2024352345 ->block address

#----------------------------- oops------------------------------

#constructor
# 1. non para 2. para 3 default constr
# # self- it contains the self variable of the current object
# 1.memoray allocation for object
# 2. memory reference returned to the object
# 3. memory reference automatically passed inside constructor
# 4. construct creates variable ar that memory reference

# class Solution:
#     def __init__(self,sal,age):
#         self.salary = sal
#         self.age = age
#
#     def display(self):
#         print(f'the salary is {self.salary} and the age  is {self.age} ')
#
# e1 = Solution(27000,23)
# e2 = Solution(28000,22)
# print(e1.__dict__)
# print(e2.display())

#built in class modules

# class Solution:
#     ''' this is class statement and thus its a empty class'''
#
# e1 = Solution()
# e2 = Solution()
#
# print(e1.__class__)
# print(e1.__doc__)
# print(e1.__module__)
#
# # isinstance() to check wheater this object belongs to this class or not
# print(isinstance(e1,Solution))

# c-2
#instance varaible and instance method

# class Solution:
#     def __init__(self,name,marks):
#         self.name = name
#         self.marks = marks
#
#     def display(self):
#         print(f'the name is {self.name} and his marks is {self.marks}')
#
#     def change_data(self):
#         self.name = input('enter the name')
#         self.marks = input('enter the marks')
#
# e1 = Solution('ashish',99)
# e2 = Solution('manav',99)
#
# e1.change_data()
# print(e1.__dict__)

#chaging the value outside the class

#-----------------class method----------------
#class method

#class varaiable
# 1. varaible made for entire class
# 2. only one copy is distributed to all objects
# 3. modification in class varaible imoar on all object
# 4. self -> object reference // cls --> class reference
#  method which works on class variable
#     first argument is class reference
#         made using decorator @classmethod

# class Employees:
#     company_name = 'saama technologies' #class variable
#     def __init__(self,name,sal):
#         self.name = name
#         self.sal = sal
#
#     @classmethod
#     def company_Det(cls):
#         cls.company_name = 'tcs'
#         print(cls.company_name)
#
# e1 = Employees('ashish',23000)
# e1 = Employees('akshay',24000)
#
# Employees.company_Det()


#-------------------insance method-------------
#instance method -> setter - to set the values of instance variable
# and getter method - to get the value of instance varaible


#---------------------static method-------------
class Bank:
    bank_name= 'BOI'
    bank_intreset = 10

    @staticmethod
    def simple_inst(prin,n):
        si = (prin*n*Bank.bank_intreset)/100
        print(si)

prin = float(input('enter the princ amnt'))
n = float(input('enter the number'))
Bank.simple_inst(prin,n)