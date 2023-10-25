# https://www.acmicpc.net/problem/1637

import sys

inp = sys.stdin.readline

N = int(inp())
conditions = []
left = float('inf')
right = -float('inf')

for _ in range(N):
    condition = tuple(map(int, inp().split()))
    conditions.append(condition)
    a, c, b = condition
    left = min(left, a)
    right = max(right, c)

right_init = right
left_sub_total = 0 # left가 업데이트 되지 않는 엣지 케이스 고려
right_sub_total = 0
while left <= right:
    mid = (left + right) // 2
    sub_total = 0
    for a, c, b in conditions:
        if mid >= a:
            sub_total += (min(mid, c) - a) // b + 1
    if sub_total % 2 == 1:
        right = mid - 1
        right_sub_total = sub_total
    else:
        left = mid + 1
        left_sub_total = sub_total

if right == right_init:
    print("NOTHING")
else:
    print(left, right_sub_total - left_sub_total)