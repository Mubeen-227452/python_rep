import math
import os
import random
import re
import sys


#
# Complete the 'sockMerchant' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY ar
#

def sockMerchant(n, ar):
    # Write your code here
    return sum([ar.count(i) // 2 for i in set(ar)])


if __name__ == '__main__':
    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))
    print([ar.count(i) // 2 for i in set(ar)])
    result = sockMerchant(n, ar)
    print(set(ar))