import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    maxi=0
    count=0
    for item in range(len(ar)):
        if ar[item]>=maxi:
            maxi=ar[item]
    for item in range(len(ar)):
        if ar[item]==maxi:
            count=count+1
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
