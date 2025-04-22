import sys
from math import factorial

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())

result = factorial(n) / (factorial(n-k) * factorial(k))

answer = result % 1000000007

print(int(answer))