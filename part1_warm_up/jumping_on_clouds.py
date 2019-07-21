#!/bin/python3

import math
import os
import random
import re
import sys


# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    # initial params
    jump_big = 2
    jump_small = 1

    jumps = 0
    pos = 0
    # we stop when we hit final index
    final_index = len(c) - 1

    while pos < final_index:
        # only jump big if does not reach passed final index and it is safe
        if ((pos + jump_big) <= final_index) and (c[pos + jump_big] == 0):
            pos += jump_big
        else:
            pos += jump_small
        jumps += 1
        print(pos, jumps)

    return jumps


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
