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
import string 

flag=True
n=get_number()
num=str(n)
digitlist=sorted(num)
for i in set(digitlist):
    count=digitlist.count(i)
    if count>1:
        flag=False
if flag==True:
    print("1")
else:
    print("0")
