#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    matches = {}
    total = 0
    for sock in ar:
        if sock not in matches:
            matches[sock] = 0
        matches[sock] += 1
    for sock in matches:
        complete_pairs = matches[sock] // 2
        total += complete_pairs
    return total

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
