import math
import os
import random
import re
import sys

def diagonalDifference(arr):
    # Write your code here
    primarysum=0
    secondarysum=0
    n=len(arr)
    for row in range(len(arr)):
        primarysum=primarysum+arr[row][row]
        secondarysum=secondarysum+arr[row][n-row-1]
    return abs(primarysum-secondarysum)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
