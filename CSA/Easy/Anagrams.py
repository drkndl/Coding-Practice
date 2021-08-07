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

count=0
maxcount=0
word_list=[]

n=get_number()

for item in range(n):
    word=get_word()
    new_word=''.join(sorted(word))
    word_list.append(new_word)
    
for item in set(word_list):
    count=word_list.count(item)
    if count>maxcount:
        maxcount=count

print(maxcount)
