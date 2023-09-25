# https://www.acmicpc.net/problem/1647

import sys
from collections import defaultdict

inp = sys.stdin.readline

def get_parent(u):
    if parent[u] == u:
        return u
    parent[u] = get_parent(parent[u])
    return parent[u]

N, M = map(int, inp().split())
links = []
parent = list(range(N + 1))

for _ in range(M):
    u, v, w = map(int, inp().split())
    links.append((w, u, v))
    
links.sort()

cost = 0
cnt = 0
for w, u, v in links:
    if cnt == N - 2:
        break
    pu = get_parent(u)
    pv = get_parent(v)
    if pu != pv:
        parent[pv] = pu
        cost += w
        cnt += 1

print(cost)