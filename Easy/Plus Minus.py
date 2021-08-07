import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    count1=0
    count2=0
    count3=0
    for num in range(len(arr)):
        if arr[num]>0:
            count1=count1+1
        elif arr[num]==0:
            count2=count2+1
        else:
            count3=count3+1
    pos=count1/len(arr)
    zero=count2/len(arr)
    neg=count3/len(arr)
    print(round(pos, 6))
    print(round(neg, 6))
    print(round(zero, 6))
    return 0

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
