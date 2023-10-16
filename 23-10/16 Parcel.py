# https://www.acmicpc.net/problem/16287

import sys

inp = sys.stdin.readline

W, N = map(int, inp().split())

elems = list(map(int, inp().split()))
dp = [None] * W

for i in range(N):
    for j in range(i + 1, N):
        s = elems[i] + elems[j]
        if s < W:
            dp[s] = (i, j)

for i in range(N):
    for j in range(i + 1, N):
        s = elems[i] + elems[j]
        if s < W:
            val = dp[W - s]
            if s < W and val:
                if i not in val and j not in val:
                    print("YES")
                    exit()

print("NO")