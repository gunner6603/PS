# https://www.acmicpc.net/problem/20303

import sys
from collections import defaultdict

inp = sys.stdin.readline

N, M, K = map(int, inp().split())
candy = list(map(int, inp().split()))
size = [1] * N
parent = list(range(N))

def get_parent(u):
    if parent[u] == u:
        return u
    parent[u] = get_parent(parent[u])
    return parent[u]

for _ in range(M):
    u, v = map(int, inp().split())
    u -= 1
    v -= 1
    pu, pv = get_parent(u), get_parent(v)
    if pu != pv:
        if pv > pu:
            pu, pv = pv, pu
        parent[pv] = pu
        candy[pu] += candy[pv]
        size[pu] += size[pv]
   
weight = []
value = []

for i in range(N):
    if parent[i] == i:
        weight.append(size[i])
        value.append(candy[i])

dp = [0] * K
for i in range(len(weight)):
    w = weight[i]
    v = value[i]
    for j in range(K - 1, -1, -1):
        if j >= w:
            dp[j] = max(dp[j], dp[j - w] + v)

print(dp[-1])