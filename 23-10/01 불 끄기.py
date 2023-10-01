# https://www.acmicpc.net/problem/14939

import sys

inp = sys.stdin.readline

chart = []

for _ in range(10):
    chart.append(int(inp().rstrip().replace('#', '0').replace('O', '1'), 2))

result = float('inf')

def count_one(n):
    cnt = 0
    while n:
        n &= n - 1
        cnt += 1
    return cnt

def apply(prev_row, prev, pprev):
    for i in range(10):
        if prev & (1 << i) > 0:
            if i == 0:
                prev_row ^= 3
            elif i == 9:
                prev_row ^= 3 << 8
            else:
                prev_row ^= 7 << (i - 1)
                
    prev_row ^= pprev
    
    return prev_row

for i in range(2**10):
    pprev = 0
    prev = i
    pushed = count_one(i)
    for prev_idx in range(10):
        prev_row = chart[prev_idx]
        cur = apply(prev_row, prev, pprev)
        if prev_idx == 9:
            if cur == 0:
                result = min(result, pushed)
                break
        pushed += count_one(cur)
        pprev = prev
        prev = cur

if result == float('inf'):
    print(-1)     
else:
    print(result)