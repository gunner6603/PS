# https://www.acmicpc.net/problem/1948

import sys
from collections import defaultdict
sys.setrecursionlimit(10**5)

inp = sys.stdin.readline
N = int(inp())
M = int(inp())

link = defaultdict(list)
indegree = [0] * (N + 1)

for _ in range(M):
    u, v, w = map(int, inp().split())
    link[u].append((v, w))
    indegree[v] += 1

s, e = map(int, inp().split())

max_dist = [0] * (N + 1)
prev_list = [[] for _ in range(N + 1)]
stack = [s]

while stack:
    u = stack.pop()
    mdu = max_dist[u]
    for v, w in link[u]:
        mdv = max_dist[v]
        cmdv = mdu + w
        if cmdv > mdv:
            max_dist[v] = cmdv
            prev_list[v] = [u]
        elif cmdv == mdv:
            prev_list[v].append(u)
        indegree[v] -= 1
        if indegree[v] == 0:
            stack.append(v)

cnt = 0
discovered = [False] * (N + 1)
def dfs(u):
    global cnt
    discovered[u] = True
    for v in prev_list[u]:
        cnt += 1
        if not discovered[v]:
            dfs(v)
dfs(e)

print(max_dist[e])
print(cnt)