# https://www.acmicpc.net/problem/2342

import sys

inp = sys.stdin.readline

def move(a, b):
    if a == 0:
        return 2
    if abs(a - b) == 2:
        return 4
    return 3

seq = list(map(int, inp().split()))

dp = [[[float('inf')] * 5 for _ in range(5)] for _ in range(len(seq))]
dp[0][0][0] = 0

for i in range(1, len(seq)):
    num = seq[i - 1]
    prev = dp[i - 1]
    cur = dp[i]
    for j in range(5):
        for k in range(j, 5):
            val = prev[j][k]
            if val != float('inf'):
                if num in (j, k):
                    cur[j][k] = min(cur[j][k], val + 1)
                # j 가 num 으로 이동
                if num < k:
                    cur[num][k] = min(cur[num][k], val + move(j, num))
                else:
                    cur[k][num] = min(cur[k][num], val + move(j, num))
                # k 가 num 으로 이동
                if num < j:
                    cur[num][j] = min(cur[num][j], val + move(k, num))
                else:
                    cur[j][num] = min(cur[j][num], val + move(k, num))

answer = float('inf')
for i in range(5):
    for j in range(i, 5):
        answer = min(answer, dp[-1][i][j])

print(answer)