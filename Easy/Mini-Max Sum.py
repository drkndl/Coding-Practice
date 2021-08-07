import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    arr.sort()
    mini=0
    maxi=0
    for item in range(len(arr)-1):
        mini=mini+arr[item]
    for item in range(len(arr)):
        maxi=maxi+arr[item]
    maxi=maxi-arr[0]
    print(mini, maxi)

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
