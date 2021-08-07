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

a = get_number()
b = get_number()
count=0
countdiv=0
for item in range(int(a), int(b)+1):
    for div in range(1, int(item/2+1)):
        if item%div==0:
            countdiv+=1
    if (countdiv+1)%2!=0:
        count+=1
    countdiv=0
print(count)
