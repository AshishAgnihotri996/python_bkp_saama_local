# import time
# from time import sleep
# import os
# from threading import Thread,main_thread,active_count,enumerate,current_thread
# videos = ['oop','constructor','destructor','file handling']
#
# class Myclass(Thread):
#     def __init__(self,val):
#         print('constructor called')
#         self.kid = val
#         Thread.__init__(self)
#
#     def compression(self):
#         print('video compression')
#
#     def run(self):
#         a = 10
#         b = 20
#         self.compression()
#         if self.kid:
#             print('suitable for kids')
#         for vid in videos:
#             print(f"{vid}started uploading")
#             sleep(0.4)
#             print(f"{vid}uploaded")
#         self.temp = a+b
#
# t1 = Myclass(False)
# t1.start()
# sleep(10)
# print("result is",t1.temp)
# for i in range(4):
#     sleep(0.4)
#     print("checking copyrights")

# def display():
#     print(main_thread())
#     for i in range(4):
#         print('hello ')
#
# def show():
#     for i in range(5):
#         print('welcome')
#
# t1 = Thread(target=display)
# print('before',t1.is_alive())
# t2 = Thread(target=show)
# t1.start()
# print('after',t1.is_alive())
# print(t1.ident)
# print(t1.native_id)
# print(os.getpid())
# t1.join()
# t2.start()
# t2.join()
# print('active_count',active_count())
# print('no of threads',enumerate())
#
# for i in range(2):
#     print('closing')

# def square(num):
#     print('finding square')
#     time.sleep(1)
#     print('square',num**2)
#
#
# def cube(num):
#     print('finding cube')
#     time.sleep(1)
#     print('cube', num ** 3)
#
# begin = time.time()
# t1 = Thread(target = square,args = (3,))
# t2 = Thread(target = cube,args = (3,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('total time taken',time.time()- begin)

# race condition
# from threading import Lock,RLock,Thread
# l = Lock()
# class Bus:
#     def __init__(self,name,available_seats,lock):
#         self.available_seats  = available_seats
#         self.name = name
#         self.lock = lock
#     def reserve(self,need_seats):
#         self.lock.acquire()
#         # print(self.lock)
#         print('available seats are ',self.available_seats)
#         if self.available_seats >= need_seats:
#             nm = current_thread().name
#             print(f"{need_seats}are allovated to {nm}")
#             self.available_seats -= need_seats
#         else:
#             print('no seats available')
#         self.lock.release()
#         # l = lock.release()
# b1 = Bus('travels',2,1)
# t1 = Thread(target=b1.reserve,args = (1,),name= 'ashish')
# t2 = Thread(target=b1.reserve,args = (2,),name= 'choti')
# t1.start()
# t2.start()

#--------------------------------Rlock
#
# from threading import *
# from time import sleep
# l = RLock()
# def get_first_line():
#     # l.acquire()
#     print('firstline')
#     # l.release()
# def get_second_line():
#     l.acquire()
#     print('second line')
#     l.acquire()
#
#
# def main():
#     l.acquire()
#     get_first_line()
#     get_second_line()
#     l.release()
# t1 = Thread(target=main)
# t1.start()
# t2 = Thread(target=get_first_line())
# t2.start()

# import threading
# from time import sleep
#
# def custom_hook(args):
#     print(args[0])
#     print(args[1])
#     print(args[2])
#     print(args[3])
#
# def display():
#     for i in range(5):
#         sleep(0.1)
#         print('hello')
#
# def show():
#     for i in range(5):
#         print('yo')
#         sleep(10)
# threading.excepthooke = custom_hook
# t1 = threading.Thread(target=display)
# t2 = threading.Thread(target=show)
# t1.start()
# t2.start()

# trafffic light ex
#
# import threading
# from time import sleep
#
# e = threading.Event()
#
# def signal_light():
#     while True:
#         print('lightr is green')
#         e.set()
#         sleep(5)
#         print("light is red")
#         e.clear()
#         sleep(5)
#         e.set()
#
# def traffic_msg():
#     e.wait()
#     while e.is_set():
#         print('youy can go')
#         sleep(0.6)
#     e.wait()
#
# t1 = threading.Thread(target=signal_light)
# t2 = threading.Thread(target=traffic_msg)
# t1.start()
# t2.start()

class Decorator:
    def __init__(self,func):
        self.function = func

    def __call__(self,a,b):
        result = self.function(a,b)
        return result**2

@Decorator
def add(a,b):
    return  a+b


print(add(2,2))