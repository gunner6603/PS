# https://www.acmicpc.net/problem/11280

import sys
sys.setrecursionlimit(10**5)

inp = sys.stdin.readline

N, M = map(int, inp().split())

link = [[] for _ in range(2*N + 1)]

for _ in range(M):
    u, v = map(int, inp().split())
    link[-u].append(v)
    link[-v].append(u)

visited = [0] * (2*N + 1)
scc_mapping = [None] * (2*N + 1)    
scc_id = 0
node_id = 0
stack = []

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
        elif not scc_mapping[v]:
            reachable_min_id = min(reachable_min_id, visited[v])
    
    if reachable_min_id == visited[u]:
        scc_id += 1
        while stack:
            p = stack.pop()
            scc_mapping[p] = scc_id
            if p == u:
                break
    
    return reachable_min_id

for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
    if not visited[-i]:
        dfs(-i)

answer = 1

for i in range(1, N + 1):
    if scc_mapping[i] == scc_mapping[-i]:
        answer = 0
        break
    
print(answer)