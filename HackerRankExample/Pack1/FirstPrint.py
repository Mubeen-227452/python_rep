from __future__ import print_function

if __name__ == '__main__':
    print("Hello, Wold!")

"""


if __name__ == '__main__':
    a = int(raw_input())
    b = int(raw_input())
    print(a + b)
    print(a - b)
    print(a * b)"""
import math
import os
import random
import re
import sys

n = int(input("enter number > "))
if n % 2 == 0 and (n in range(2, 6) or n > 20):
    print("Not ", )

print("Weired")

print(*range(1, int(input()) + 1), sep='')

i = int(input())
lis = list(map(int,input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print(max(lis))

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    print("{0:.2f}".format(sum(query_scores)/(len(query_scores))))
