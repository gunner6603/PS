# https://www.acmicpc.net/problem/11689

import sys

inp = sys.stdin.readline

N = int(inp())
result = N

for i in range(2, int(N**0.5) + 1):
    if N % i == 0:
        result -= result // i
        while N % i == 0:
            N //= i

if N > 1:
    result -= result // N
    
print(result)