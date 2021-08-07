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

n=get_number()
k=get_number()
arr=[]
count=0 

for item in range(int(n)):
    num=get_number()
    arr.append(num)
    
for num in set(arr):
    if arr.count(num)>=k:
        count+=1
        
print(count)
