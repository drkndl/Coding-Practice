# a simple parser for python. use get_number() and get_word() to read
def parser():
    while 1:
        data = list(input().split(' '))
        for number in data:
            if len(number) > 0:
                yield(number)   

input_parser = parser()

def get_word():
    global input_parser
    return next(input_parser)

def get_number():
    data = get_word()
    try:
        return int(data)
    except ValueError:
        return float(data)

# numpy and scipy are available for use
import numpy
import scipy
import math

n=get_number()

arr=[]
for item in range(int(n)):
    num=get_number()
    arr.append(num)

count=0
arr1=[]
arr2=[]
arr0=[]
for item in range(len(arr)):
    if int(arr[item]%3)==1%3:
        arr1.append(arr[item])
    elif int(arr[item]%3)==2%3:
        arr2.append(arr[item])
    else:
        arr0.append(arr[item])

count=len(arr1)*len(arr2)+math.factorial(len(arr0))/(math.factorial(2)*math.factorial(len(arr0)-2))
print(int(count))
