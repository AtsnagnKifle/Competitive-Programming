#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'insertionSort1' function below.
#
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#
# 2 4 6 8 3
# Sample Output

# 2 4 6 8 8
# 2 4 6 6 8
# 2 4 4 6 8
# 2 3 4 6 8


def insertionSort1(n, arr):
    # Write your code here
    no = arr[-1]
    bo = False
    for i in range(n-1, 0, -1):
        if arr[i-1] <= no:
            arr[i] = no
            print(" ".join([str(j) for j in arr]))
            bo = True
            break
        else:
            arr[i] = arr[i-1]
            print(" ".join([str(j) for j in arr]))
    if not bo:
        arr[0] = no
        print(" ".join([str(j) for j in arr]))


if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
