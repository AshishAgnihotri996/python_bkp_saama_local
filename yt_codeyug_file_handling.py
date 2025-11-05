# f = open('filehandling_demo.txt','r',encoding='utf-8',buffering= 1000)
# if f:
#     print(f.name)
#     f.close()
#     print(f.closed)
# print(type(f))
#
# import os
# filename = input('enter the filename')
# if os.path.isfile(filename):
#     f = open(filename,'r')
#     f1 = open(filename,'r')
#     f2 = open(filename,'r')
#     print(f.readline(),end= " ")
#     print(f2.readlines())
#     for i in f2:
#         print(i, end= " ")
#     print(f1.readline())
#     print(f.seek(2))
#     f.close()
# else:
#     print('not found')


#problem solving

# f= open('filehandling_demo.txt','r')
# words = 0
# line = 0
# chars = 0
#
# for line in f:
#     line += 1
#     line = line.strip('\n')
#     chars += len(line)
#     list1 = line.split()
#     words = len(list1)
#
# f.close()
# print(words)
# print(line)
# print(chars)

f = open('demo.txt','w')
f1 = open('filehandling_demo.txt','r')

for line in f1:
    f.write(line)
f.close()
f1.close()




