# https://www.acmicpc.net/problem/17383

import sys
from bisect import bisect_right

inp = sys.stdin.readline

N = int(inp())
times = list(map(int, inp().split()))

times.sort()

left = 1
right = 10**9
while left <= right:
    mid = (left + right) // 2 # time unit
    single_time_unit_cnt_needed = 1
    i = 1
    for i in range(1, 10**9 // mid):
        upper = bisect_right(times, mid*(i + 2))
        lower = bisect_right(times, mid*(i + 1))
        single_time_unit_cnt_needed += (upper - lower)*i
        if upper == N:
            break
    single_time_unit_cnt = bisect_right(times, mid)
    if single_time_unit_cnt_needed > single_time_unit_cnt:
        left = mid + 1
    else:
        right = mid - 1
        
print(left)