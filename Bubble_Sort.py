#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countSwaps' function below.
#
# The function accepts INTEGER_ARRAY a as parameter.
#


def countSwaps(a):
    # Write your code here
    no_swap = 0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j] > a[j+1]:
                no_swap += 1
                tmp = a[j]
                a[j] = a[j+1]
                a[j+1] = tmp
    print("Array is sorted in {} swaps.".format(no_swap))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))


if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
