# https://www.acmicpc.net/problem/11280

import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)

inp = sys.stdin.readline

N, M = map(int, inp().split())

link = [[] for _ in range(2*N + 1)]

for _ in range(M):
    u, v = map(int, inp().split())
    link[-u].append(v)
    link[-v].append(u)

visited = [0] * (2*N + 1)
scc_list = [None] * (2*N + 1)    
scc_id = 0
node_id = 0
stack = []
val = [None] * (N + 1)

def dfs(u):
    global node_id
    global scc_id
    node_id += 1
    visited[u] = node_id
    stack.append(u)
    
    reachable_min_id = node_id
    for v in link[u]:
        if not visited[v]:
            reachable_min_id = min(reachable_min_id, dfs(v))
        elif not scc_list[v]:
            reachable_min_id = min(reachable_min_id, visited[v])
    
    if reachable_min_id == visited[u]:
        scc_id += 1
        while stack:
            p = stack.pop()
            scc_list[p] = scc_id
            if val[abs(p)] is None:
                val[abs(p)] = 1 if p > 0 else 0
            if p == u:
                break
    
    return reachable_min_id

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
    if not visited[-i]:
        dfs(-i)

for i in range(1, N + 1):
    if scc_list[i] == scc_list[-i]:
        print(0)
        exit()
    
print(1)

for i in range(1, N + 1):
    v = val[i]
    print(v, end=" ")