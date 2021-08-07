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
k=get_number()
arr=[]
sum=0

for item in range(int(n)):
    glass=get_number()
    arr.append(glass)
    
arr.sort()
for i in range(int(k)):
    sum=sum+arr[i]

bottle=sum/100
print(math.ceil(bottle))
