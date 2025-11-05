# import sys
#
# x =  int(input('enter the first number'))
# y =  int(input('enter the first number'))
#
# try:
#     ans = x/y
#     print(ans)
# except:
#     print(sys.exc_info()[0])
#     print(sys.exc_info()[1])


#--- raise exception
# try:
#     x = int(input('enter the age'))
#     if x < 0:
#         raise ValueError('error')
#     print('age:',x)
# except ValueError as var:
#     print(var)
#
# print('rest of the code')
#
# class FiveDivisionError(Exception):
#     def __init__(self):
#         print('cannot divide by five')
#
# try:
#     x = int(input('enter the first number'))
#     y =  int(input('enter the first number'))
#     if y == 5:
#         raise FiveDivisionError
#     ans = x/y
#     print(ans)
#
# except (FiveDivisionError,ZeroDivisionError) as e:
#     print(e)
import time


class BalanceExceptionError(Exception):
    pass
class AttemptExceptionError(Exception):
    pass
attempt= 1
def withdraw():
    global attempt
    saved_pin = 1605
    balance = 12000
    pin = int(input('enter the pin'))
    if pin == saved_pin:
        try:
            amt = float(input('enter the amount to withdraw'))
            temp_bal = balance-amt
            if temp_bal <1000:
                raise BalanceExceptionError('cant trans')
            balance = balance - amt
            print(balance)
        except Exception as e:
            print(e)
    else:
        ans = input('do you wabnt to contiue press y')
        if ans.lower() == 'y':
            attempt+=1
            try:
                if attempt == 4:
                    raise AttemptExceptionError('too many attemps your accouint hgas been locked')
            except Exception as e:
                print(e)
                time.sleep(3600)
            else:
                withdraw()
        else:
            print('thank you')
            return
withdraw()
