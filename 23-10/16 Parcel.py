# https://www.acmicpc.net/problem/16287

import sys

inp = sys.stdin.readline

W, N = map(int, inp().split())

elems = list(map(int, inp().split()))
dp = [False] * W

for i in range(N):
    ei = elems[i]
    for j in range(i + 1, N):
        s = ei + elems[j]
        if s < W and dp[W - s]:
            print("YES")
            exit()
    for j in range(i):
        s = ei + elems[j]
        if s < W:
            dp[s] = True
            
print("NO")