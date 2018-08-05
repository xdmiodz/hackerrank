#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the nonDivisibleSubset function below.
def nonDivisibleSubset(k, S):
    sets = Counter(item % k for item in S)
    total_len = int(sets[0] > 0)
    midpoint = k // 2 + 1 if k % 2 == 0 else (k + 1) // 2
    for p1 in range(1, midpoint):
        p2 = k - p1
        if p2 != p1:
            total_len += max(sets[p1], sets[p2])
        else:
            total_len += 1
    return total_len


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    S = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, S)

    fptr.write(str(result) + '\n')

    fptr.close()
