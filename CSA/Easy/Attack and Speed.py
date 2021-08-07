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

a=get_number()
s=get_number()
k=get_number()
x=get_number()
y=get_number()

i=(s+k*y-a)/(x+y)

if i%1==0 and i>=0 and i<=k:
    print(int(i))
else:
    print("-1")
