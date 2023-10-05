# https://www.acmicpc.net/problem/2150

import sys
from collections import defaultdict
sys.setrecursionlimit(10**6)

inp = sys.stdin.readline

V, E = map(int, inp().split())
link = defaultdict(list)
for _ in range(E):
    u, v = map(int, inp().split())
    link[u].append(v)
    
stack = []
visited = [0] * (V + 1)
made = [False] * (V + 1)
node_id = 0
scc_map = dict()

def dfs(u):
    global node_id
    node_id += 1
    visited[u] = node_id
    stack.append(u)
    
    reachable = node_id
    for v in link[u]:
        if not visited[v]:
            reachable = min(dfs(v), reachable)
        elif not made[v]:
            reachable = min(visited[v], reachable)
    
    if reachable == visited[u]:
        scc_nodes = []
        while stack:
            p = stack.pop()
            made[p] = True
            scc_nodes.append(p)
            if p == u:
                break
        scc_nodes.sort()
        scc_map[scc_nodes[0]] = scc_nodes
    
    return reachable

for u in range(1, V + 1):
    if not visited[u]:
        dfs(u)

print(len(scc_map.keys()))
for k in sorted(scc_map.keys()):
    scc_map[k].append(-1)
    print(*scc_map[k])