# https://www.acmicpc.net/problem/20040

import sys
sys.setrecursionlimit(10**6)

inp = sys.stdin.readline

def get_parent(u):
    if parent[u] == u:
        return u
    parent[u] = get_parent(parent[u])
    return parent[u]

N, M = map(int, inp().split())
parent = list(range(N))
finished = False
finished_time = None

for i in range(1, M + 1):
    u, v = map(int, inp().split())
    if finished:
        continue
    pu = get_parent(u)
    pv = get_parent(v)
    if pu != pv:
        parent[pv] = pu
    else:
        finished = True
        finished_time = i
        
if finished:
    print(finished_time)
else:
    print(0)