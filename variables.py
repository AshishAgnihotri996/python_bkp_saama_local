# sal = int(input('enter your salary'))
# rate = 0
#
# if sal >= 2000:
#     print('you are eligible for mortage')
#     credit_Score = int(input('enter your credit score'))
#     if credit_Score >800:
#         rate =4
#         print('intrest rate is 4')
#     elif credit_Score >750:
#         rate =6
#         print('intrest rate is 6')
#     else:
#         rate = 8
#         print('intrest rate is 8')
#     disab = str(input('are you disabled  Y or N'))
#     if disab =='Y':
#         rate = rate-2
#     print('you rate is',rate)
# else:
#     print('sorry you are not eligble')
#
# mini_Burger = 5
# normal_Burger = 8
# large_Burger = 10
# mushroom_mini =1
# mushroom_normal =1
# mushroom_large =2
# exetra_Cheese =1
#
# size = str(input('enter the size of the burger'))
# if size == 'N':
#     size = normal_Burger
#     print(size)
#
# else:
#     print('sorry')

# mini_Burger = 5
# normal_Burger = 8
# large_Burger = 10
# mushroom_mini = 1
# mushroom_normal = 1
# mushroom_large = 2
# exetra_Cheese = 1
#
# try:
#     size = str(input('enter the size of the burger'))
# except:
#     print('enter the size only')
#     size = str(input('enter the size of the burger'))
# else:
#     if size == 'N':
#         size = normal_Burger
#         print(size)
#         add_mushroom = str(input('do you want to add mushroom ?'))
#         if add_mushroom == 'Y':
#             size = size + 1
#             exetra_Cheese = str(input('do you want to add cheese ?'))
#         if exetra_Cheese == 'Y':
#             size = size + 1
#             print('your final bill is:',size)
#
#         else:
#             if size =='L':
#                 size = large_Burger
#                 print(size)
#     else:
#         print('sorry')
# finally:
#     print("Thanks for using our calculator!")

# import math
#
# # r = int(input("Enter Radius"))
# # res= r * r
# # print(res)
#
# import math
#
# fact = math.factorial(4)
# print(f"The factorial of 4 is : {fact}")


# import random
#
# head = 1
# tail = 0
#
# res = random.randint(0,1)
# print(res)
#
# if res == 1 :
#     print('its head')
# else:
#     print('tail')

#reversal string

# a = str(input('enter the word for reversal string'))
# index= -1
# b = -1  * len(a)
#
# while index >= b:
#     letter = a[index]
#     print(letter)
#     index -=1

# num = input('enter the digit')
# sum = 0
# for i in num:
#     sum += int(num)
# print(sum)


# def data_count (word,letter):
#     counter = 0
#     for i in word:
#         if i == letter:
#             counter+=1
#
#     return counter
#
# print(data_count('tejaswini','a'))

# def first_last_characters(word):
#     abb = word[:2]+word[-2:]
#     return abb
# print(first_last_characters('ashishagnihotri'))

# custom_string = 'I love Python.....'
#
# custom_string = custom_string.replace('.','!',3)
# print(custom_string)

#find and split

# a = "my email is ashishagnihtori996@gmail.com.saama.eu id"
# at_index = a.find('@')
# print(at_index)
# after_space = a.find(' ',at_index)
# print(after_space)
# print(a[at_index+1:after_space])

# custom_string = 'X-MAPDS-Confidence:0.8475'
# after_colon = custom_string.find(':')
# a = custom_string[after_colon+1:]
# a = float(a)
# print(a)

# Function to print a half pyramid pattern
def half_pyramid(n):
	for i in range(1, n + 1):
		for j in range(1, i + 1):
			print("* ", end="")
		print("\r")

for i in range(1, 0, - 1):
    for j in range(1, i - 1):
        print("* ", end="")
    print("\r")

n = 5
half_pyramid(n)

