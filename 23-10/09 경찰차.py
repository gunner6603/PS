# https://www.acmicpc.net/problem/2618

import sys

inp = sys.stdin.readline

N = int(inp())
W = int(inp())

loc = [(1, 1), (N, N)] + [tuple(map(int, inp().split())) for _ in range(W)]

dp = [[None] * (W + 2) for _ in range(W + 1)]
dp[0][0] = (0, 1, None) # cost, car, prev_idx

def dist(loc1, loc2):
    x1, y1 = loc1
    x2, y2 = loc2
    return abs(x1 - x2) + abs(y1 - y2)

for i in range(2, W + 2):
    current_case = loc[i]
    cur_dp = dp[i - 1]
    for j, elem in enumerate(dp[i - 2]):
        if elem is None:
            continue
        car1_prev_loc = loc[j]
        cost, car1_num, _ = elem
        car2_prev_loc = loc[i - 1]
        sol1 = (cost + dist(car1_prev_loc, current_case), 3 - car1_num, j) # i - 1에 저장
        sol2 = (cost + dist(car2_prev_loc, current_case), car1_num, j) # j에 저장
        if cur_dp[i - 1] is None or cur_dp[i - 1][0] > sol1[0]:
            cur_dp[i - 1] = sol1
        if cur_dp[j] is None or cur_dp[j][0] > sol2[0]:
            cur_dp[j] = sol2

min_val = float('inf')
start_idx = None
for i, elem in enumerate(dp[-1]):
    if elem is None:
        continue
    if min_val > elem[0]:
        min_val = elem[0]
        start_idx = i
print(min_val)

rev_list = []
i = W
j = start_idx
while i >= 1:
    cost, car, prev_idx = dp[i][j]
    rev_list.append(3 - car)
    i -= 1
    j = prev_idx
        
for car in reversed(rev_list):
    print(car)