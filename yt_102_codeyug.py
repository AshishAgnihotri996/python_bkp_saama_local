# n = int(input('enter the number of tersms'))
# first = 0
# second = 1
# if n<=0:
#     print('enter postive number')
# elif n ==1:
#     print('fibonacci series is ',first)
# else:
#     for i in range(n):
#         print(first,end = " ")
#         temp = first
#         first = second
#         second = temp+first
#

# print name using recusseion
# count =1
# def printName(name):
#     global count
#     if count <= 10 :
#         print(name)
#         count+=1
#         printName(name)
# printName('ashish')


# print the data without using loop

# n  = eval(input('enter the elements'))
# start = eval(input('etner the staring index'))
# end = eval(input('etner the end index'))
#
# def iterate(n,start,end):
#     if start <0 or start >= end or end >len(n):
#         return
#     else:
#         print(n[start])
#         iterate(n,start+1,end)
# iterate(n,start,end)

# reverse the string
# str1 = 'ashish agnihotri'
# print(" ".join(str1.split()[::-1]))

#

# str1 = "a,a,a,b,b,b,bf,f,f,r,r,r,ty,t,h,h,h"
# str1 = str1.split(",")
# visited =[]
# ls=[]
# for ch in str1:
#     if ch not in  visited:
#         print(f"{ch},{str1.count(ch)}")
#         visited.append(ch)

# twin prime numbers

# def isPrime(num):
#     if num <1 :
#         return False
#     for i in range(2,num):
#         if num %i ==0:
#             return False
#     return True
#
# n1 = int(input('etner the first num'))
# n2 = int(input('etner the second num'))
#
# if isPrime(n1) and isPrime(n2):
#     if abs(n1 -n2) == 2:
#         print(f"{n1} and {n2} are twin prime numbers")
#     else:
#         print(f"{n1} and {n2} are not twin prime numbers")
# else:
#     print('are not a prime number')
#  num_of_subs = 5
#  for std in student_Data:
#      per = sum(num_of_subs[std]['details']['marsks'])/num_of_subs
#      print(f"{std}")

# str1 = input('etner the string')
# upper_Str = ""
# for ch in str1:
#     asc = ord(ch)
#     if asc > 64 and asc<91:
#         upper_Str = upper_Str+chr(asc+32)
#     else:
#         upper_Str = upper_Str+chr(asc)
# print('lower case string',upper_Str)

#
# def changeAds(nums):
#     b = bin(nums)
#     b = b[2:len(b)]
#     b1 = ""
#     for bit in b:
#         if bit =='1':
#             b1 = b1+'0'
#         else:
#             b1 = b1 +'1'
#     sum1 = 0
#     for i in range(len(b1)):
#         sum1 =sum1 +(int(b1[i])*(2**(len(b1)-(i+1))))
#     return sum1
# print(changeAds(500))

# def maxArray(arr):
#     n = len(arr)
#     if n <2 :
#         return False
#     a = arr[0]
#     b = arr[1]
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if (arr[i]*arr[j] > (a*b)):
#                 a = arr[i]
#                 b = arr[j]
#
# arr = eval(input('enter the string'))
# print(arr)
# maxArray(arr)


# def rectangle(sticks,lengths):
#     arr =[]
#     for stk in lengths:
#         if lengths.counts(stk) >=2 or stk not in arr:
#             arr.append(stk)
#     max_Area = 0
#     for i in range(len(arr)):
#         for j in range(i+1,len(arr)):
#             if arr[i]*arr[j] > max_Area:
#                 max_Area = arr[i]*arr[j]
#     return max_Area

# print(rectangle(5,[1,8,1,8,8])

# f1 = open("filehandling_demo.txt",'r')
# f2 = open("filehandling_demo.txt",'w')
# modified_oputput = []
# data = f1.readlines()
#
# header = data[0]
# modified_oputput.append(header)
#
# for record in data[1:len(data)+1]:
#     my_list = record.split("|")
#     salary = float(my_list[2])
#     if salary > 35000:
#         bonus= 2000
#         modified_oputput(f"mylist[0]")
#
#
# f1.close()
# f2.close()


#list comrehension list / set /dictionary -> compreHENSION

# syntaz=[ expression | loop  | condition ]

# num = [3,6,8,12,14,15]
# sq =[]
# for i in num:
#     if i%2==0:
#         sq.append(i*i)
#     else:
#         sq.append(i*i*i)
#
# print(sq)

# print([i*i if i%2==0 else i*i*i for i in num])
# print([i*j for i in range(3,10) for j in range(1,12)])

# for finding all possible  substring

# str1 = 'ashish'
# ot= []
# for i in range(len(str1)):
#     for j in range(i+1,len(str1)+1):
#         ot.append(str1[i:j])
# print(ot)

# table
# while True:
#     x = int(input('enter the number'))
#     for i in range(1,11):
#         print(f"{x}*{i}'=='{x*i}")
#     ans = input('do u want to contier')
#     ans.lower()
#     if ans != 'y':
#         break


# factorial - math / recussion/ loop
# import math
# x= int(input('enter the number'))
# a = math.factorial(x)
# print(a)

# by loop
# x= int(input('enter the number'))
# ot = 1
# for i in range(x,0,-1):
#     ot = ot*i
# print(ot)

# str1= 'aaaabbbbvvvvccccffffgggggjjkk'
# op = ""
# char =str1[0]
# count = 0
#
# for ch in str1:
#     if ch == char:
#         count+=1
#     else:
#         op = op + str(count) + char
#         count =1
#         char = ch
# print(op)

#docstring

#sort and sorted
# op =[]
# def mybad(l):
#     for i in l:
#         if i%2==0:
#             op.append(i)
#     return op
#
# l = [1,2,5,8,45,98,56,32,1,24,58,7]
# l.sort(key=mybad)
# print(l)


# data=('ashihs',234,4324,4234)
# print(sorted(data))

# str1 = '1=a&b=3&name=ashish'
# ot =[]
# for ele in str1.split("&"):
#     ot.append(ele.split("="))
#
# print(ot)

#upper case alternate method
#with inbuilt method
#
# str1 = 'aShIsH'
# str2= ""
# i=0
# while i < len(str1):
#     if i==0:
#         str2= str2+str1[i].upper()
#     else:
#         str2 = str2+str1[i].swapcase()
#     i+=1
# print(str2)

#without methods


#example
# str1 = "AC*wvn/:#ewesdf$#45$#4$@2kh3b4"
# temp = ""
# data = []
# for ch in str1:
#     if ch.isdigit():
#         temp =temp+ch
#     elif len(temp)!=0:
#         data.append(eval(temp))
#         temp= ""
# data.sort()
# print(data)

# l = [1,2,3,4,5,6,7,8,9]
# largest = l[0]
# second_largest= l[0]
#
# for i in range(len(l)):
#     if l[i] > largest:
#         largest = l[i]
#
# for i in range(len(l)):
#     if l[i] > second_largest and l[i] != largest:
#         second_largest = l[i]
# print(second_largest)
#
# x = 'ashishagnihotri'
#
# print(x[-1:-5:-3])


#voting system
# v1 = input('enter the name of the candidat')
# v2 = input('enter the name of the candidat')
# v1_vote =[]
# v2_vote =[]
# voted=[]
# voters_id=[101,102,103,104,105,106]
# no_of_voters = len(voters_id)
# while True:
#     if voters_id ==[]:
#         print('voting is over')
#         if v1_vote > v2_vote:
#             print('candidtae won the election',v1)
#         elif v2_vote> v1_vote:
#             print('candidate wono the election',v2)
#         elif v1_vote == v2_vote:
#             print('tied')
#
#     else:
#         voter = int(input('enter the id'))
#         if voter in voted:
#             print('already voted')
#         else:
#             if voter in voters_id:
#                 print(v1,v2)
#                 choice = int(input('eenter your id'))
#                 if choice == 1:
#                     v1_vote+=1
#                 elif choice ==2 :
#                     v2_vote+=2
#                 voters_id.remove(voter)
#                 voted.append(voter)
#
#             else:
#                 print('u ar nopt allowed to vote')

# import copy
# a = [1,2,3,4,5,6,7,8,98]
# b = copy.deepcopy(a)
# c = copy.copy(a)
# print(id(a))
# print(id(b))
# print(a)
# print(b)

# str1 = 'abaababc'
# ot = ""
# mydict = {}
# for ch in str1:
#     if ch not in mydict:
#         mydict[ch] =1
#         print(ch,end="")
#     else:
#         mydict[ch] = mydict[ch] +1
#         print(ch*mydict[ch],end="")


# str1 = '3135468746814321'
# i = 0
# ot = []
# while i < len(str1)-1:
#     if i%2==0:
#         ot.append((str1[i],str1[i+1]))
#     else:
#         ot.append((str1[i], int(str1[i + 1])))
#     i+=1
# print(ot)


#----------------------------------------
# def Bonus():
#     bonus = 2000
#     return bonus
#
# def Salary_Bonus(b):
#     salary = 10000
#     a = Bonus() + salary
#     print(a)
#
# alary_Bonus(Bonus)

# def demo():
#     return  'hello worlfd'
#
# def outer(d):
#     print(d()) -- 1
#     return d -- 2
# d2 = outer(demo)
# print(d2())


#IFEE function

# print((lambda x,y :x+y)(10,21))

#filter function
import time

nu = [12,343,564,21,45,12,23,45,65,45,12,21,22,25,22,29,2,65,65]
#
# def even_fun(nu):
#     if nu%2==0:
#         return True
# x = list(filter(even_fun,nu))
# print(x)


# x = list(filter(lambda x:x>45 and x<300,nu))
# print(x)

# lap = {'hp':50000,'lenovo':60000,'asus':35000,'mac':12000}
# bud = int(input('enter your budget'))
# def bugget(ele):
#     if lap[ele] <= bud:
#         return True
#     else:
#         return False
#
# x = list(filter(bugget,lap))
# print(x)

#MAP() function
li = [1,2,3,4,5,6,7,8,9]
# x = list(map(lambda x:x*x,li))
# print(x)

#reduce()

# import functools
#
# def func(a,b):
#     return a+b
#
# x = (functools.reduce(func,li))
# print(x)


#LEGB Rule
# x=200
# def outer():
#     x =100
#     def inner():
#         nonlocal x
#         x = x+20
#         print(x)
#     inner()
# outer()

# static method

# class Bank:
#     bank_name = 'boi'
#     interest = 12.25
#     @staticmethod
#     def simple_interest(princ,n):
#         si = princ * n * Bank.interest
#         print(si)
#
# princ = int(input('enter the princple amount'))
# n = int(input('enrter the of years'))

# Bank.simple_interest(princ,n)

#constructor overrodding

# class Father:
#     def __init__(self):
#         print('father cons')
#         self.veh = 'scooter'
#
# class Son(Father):
#     def __init__(self):
#         print('sons cons')
#         self.veh = 'bmw'
#
# s = Son()
# print(s.__dict__)

#function function

# class Computer:
#     def __init__(self,ram,storage):
#         self.ram = ram
#         self.storage = storage
#         print('computer constructor called')
#
# class Mobile(Computer):
#     def __init__(self,ram,storage):
#         super().__init__(ram,storage)
#         self.model  = 'iphone2'
#         print('mobile constructor called')
#
# m = Mobile('23ram','234storage')
# print(m.__dict__)


# hierachical inheritance

# class Parent:
#     def __init__(self,name,age):
#         self.name =name
#         self.age = age
#     def display(self):
#         print('parent display method')
#
# class Child1(Parent):
#     def __init__(self):
#         self.marks = marks
#     def display1(self):
#         print('child1 display method')
#
# class Child2(Parent):
#     def __init__(self,salary,name,age):
#         super().__init__(name,age)
#         self.salary = salary
#     def display2(self):
#         print('chid 2 display method')
#
# a = Child2(122,'ashish',25)
# print(a.__dict__)
# a.display2()

#multiple inhgeritance


class Parent1:
    def __init__(self):
        self.state = 'delhi'
        print('parent1 constructor called')

# class Parent2:
#     def __init__(self):
#         super().__init__()
#         self.state = 'mumbai'
#         print('parent2 constructor called')
#
# class Child(Parent1,Parent2):
#     def __init__(self):
#         super().__init__()
#         self.state = 'pune'
#         print('child constructor called')
#
# a = Child()
# print(a.state)

# class Cart:
#     def __init__(self,b1,b2,b3):
#         self.b1 = b1
#         self.b2 = b2
#         self.b3 = b3
#
#     def __len__(self):
#         print('the length of the cart are:')
#         return len(self.b1)+ len(self.b2)+len(self.b3)
#
# s = Cart(['asdf','asfd','adf'],['fasdf','fam','fa','fas'],['asdf'])
# print(len(s))


#operator overloading

# a = 12
# b=234
# print(a+b)
# print(a.__add__(b))
# print(int.__add__(a,b))

#
# class Book:
#     def __init__(self,title,pages):
#         self.title = title
#         self.pages = pages
#
#     def __add__(self, other):
#         total = self.pages+other.pages
#         return Book('all nbooks',total)
#
#     def __str__(self):
#         return str(self.pages)
#
# b1 = Book('ashsih',234)
# b2 = Book('choti',234)
# b3 = Book('agnihotri',234)
# b4 = Book('agnihotri',234)
# b5 = Book('agnihotri',234)
# print('total number of books are',b1+b2+b3+b4+b5)


# operator >

# class Money:
#     def __init__(self,name,fare):
#         self.name = name
#         self.fare = fare
#
#     def __gt__(self, other):
#         return b1.fare > other.fare
#
# b1 = ('ashish',453454)
# b2 = ('ashdfaish',453454)
# print(b1>b2)

#nested class

# class Student:
#     def __init__(self,name,roll,dd,mm,yy):
#         self.name = name
#         self.roll = roll
#         self.dob = self.DOB(dd,mm,yy)
#     def display(self):
#         print(f"name{self.name} and roll is{self.roll}")
#         self.dob.display()
#
#     class DOB:
#         def __init__(self,dd,mm,yy):
#             self.dd= dd
#             self.mm= mm
#             self.yy = yy
#
#         def display(self):
#             print(f"{self.dd}/{self.mm}/{self.yy}")
# s1 = Student('ashish',234,12,22,45)
# s1.display()

#poly with inheritance

# class cars:
#     def __init__(self,car,color,price):
#         self.car = car
#         self.color = color
#         self.price = price
#
#     def get_Details(self):
#         print('car name',self.car)
#         print('color is',self.color)
#         print('price',self.price)
#
#     def gear(self):
#         print('the gear is 6')
#
#     def speed(self):
#         print('maximum speed is 100km/h')
#
# class truck(cars):
#
#     def gear(self):
#         print('the gear is 7')
#
#     def speed(self):
#         print('maximum speed is 140km/h')
#
# t = truck('bmw','red',150000)
# c = cars('omni','white',80000)
# c.gear()

# to change the data of another class

# class Solution:
#     def __init__(self,id,name,sal):
#         self.id = id
#         self.name = name
#         self.sal = sal
#
#     def display(self):
#         print(f"{self.id},{self.name},{self.sal}")
#
# class Change:
#     @staticmethod
#     def changes(e1):
#         e1.sal = e1.sal +4545
#         e1.display()
#
# e1 = Solution(101,'ashish',60000)
# Change.changes(e1)

#class decorator
# class Decorator:
#     def __init__(self,func):
#         self.function = func
#     def __call__(self,a,b):
#         result = self.function(a,b)
#         return result ** 2
# @Decorator
# def add(a,b):
#     return a+b
# print(add(2,3))

#example 2
# class Decorator:
#     def __init__(self,func):
#         self.function = func
#
#     def __call__(self,*args):
#         try:
#             if any([isinstance(i,str)for i in args]):
#                 raise TypeError('cannot pass strigs')
#             else:
#                 return self.function(*args)
#         except Exception as obj:
#             print(obj)
# @Decorator
# def add(*args):
#     sum =0
#     for i in args:
#         sum = sum+i
#     return sum
# print(add(10,20,30,40,50,60,70))
# print(add(10,200,30,40,50,60,70))

#circular reference

# class Empoyee:
#     def __init__(self,obj2):
#         self.obj2 = obj2
#
#     def __del__(self):
#         print('employee destructor calleed')
#
# class Account:
#     def __init__(self,num):
#         self.num = num
#         self.obj1 =Empoyee(self)
#
#     def __del__(self):
#         print('accound destrucot calleed')
#
# ac = Account(234)
# del ac
# time.sleep(5)

# class Add:
#     def __init__(self,a,b):
#         self.a= a
#         self.b = b
#
#     def __call__(self,a,b):
#         return a+b
# a1 = Add(23,3453)
# print(a1(23,453))
# print(callable(a1))

# abstarct

# from abc import ABC,abstractmethod
#
# class Car(ABC):
#     @abstractmethod
#     def mileage(self):
#         pass
#     def color(self):
#         print('white')

#pickling and unpickling

# import pickle
# data = ['adhgfikaf',2345,234]
# byte =pickle.dumps(data)
# print(byte)
# data1 = pickle.loads(byte)
# print(data1)
# f = open('xyz.txt','wb')
# pickle.dumps(data,f)
# f.close

#json file
# import json
# data = {
#     'age':21,
#     'city' :'nashik',
#     'name': 'ashish'
# }
# f= open('data.json',mode='w')
# o = json.dump(data,f,indent=2,sort_keys=True)
# print(o)
# print(type(o))

import json
sports=['cricket','tennis','fottball','fsadf']

data = dict(list(enumerate(sports,1)))
f = open('data.json','w')
json.dump(data,f)

f.close()