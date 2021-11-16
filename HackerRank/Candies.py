#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
def candies(n, arr):
    candies = [1 for i in range(n)]

    prev = 0

    for i in range(len(arr)-1):
        le = arr[i]
        ri = arr[i+1]

        if le < ri:
            candies[i+1] = candies[i] + 1
        elif le > ri:
            if candies[i] == 1:
                for e in range(i, -1, -1):
                    if arr[e] > arr[e+1] and candies[e] <= candies[e+1]:
                        candies[e] += candies[e+1] - candies[e] + 1
                    else:
                        break
            else:
                candies[i+1] = 1 
    return sum(candies)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
n
