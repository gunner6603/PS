# https://www.acmicpc.net/problem/4386

import sys
from heapq import heappush, heappop

inp = sys.stdin.readline

N = int(inp())
stars = [tuple(map(float, inp().split())) for _ in range(N)]

def distance(s1, s2):
    x1, y1 = s1
    x2, y2 = s2
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5

def find(u):
    if parent[u] == u:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu < pv:
        parent[pv] = pu
        return True
    elif pu > pv:
        parent[pu] = pv
        return True
    return False
    
heap = []
for i in range(N):
    for j in range(i + 1, N):
        d = distance(stars[i], stars[j])
        heappush(heap, (d, i, j))

parent = list(range(N))
cost = 0

while heap:
    d, u, v = heappop(heap)
    if union(u, v):
        cost += d

print(cost)    