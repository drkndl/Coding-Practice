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
import numpy as np
import scipy

num_shoes=np.zeros((101,2))
n=get_number()
for item in range(int(n)):
    size=get_number()
    typeo=get_word()
    if typeo=='L':
        typeo=0
    else:
        typeo=1
    num_shoes[int(size)][int(typeo)]+=1

#print(num_shoes)
answer=0
for item in range(101):
    answer+=min(num_shoes[item][0], num_shoes[item][1])
    
print(answer)
