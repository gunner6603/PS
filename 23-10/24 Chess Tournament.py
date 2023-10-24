# https://www.acmicpc.net/problem/13344

import sys
from collections import defaultdict

sys.setrecursionlimit(10**6)
inp = sys.stdin.readline

N, M = map(int, inp().split())
games = []
parent = list(range(N))

def find(u):
    if parent[u] == u:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def union(u, v):
    pu = find(u)
    pv = find(v)
    if pu != pv:
        parent[pu] = pv

for _ in range(M):
    p1, symbol, p2 = inp().split()
    p1 = int(p1)
    p2 = int(p2)
    if symbol == "=":
        union(p1, p2)
    else:
        games.append((p1, p2))

link = defaultdict(list)
indegree = [0] * N
for p1, p2 in games:
    pp1 = find(p1)
    pp2 = find(p2)
    if pp1 == pp2:
        print("inconsistent")
        exit(0)
    link[pp1].append(pp2)
    indegree[pp2] += 1

stack = []
for u in range(N):
    if parent[u] == u and indegree[u] == 0:
        stack.append(u)

while stack:
    u = stack.pop()
    for v in link[u]:
        indegree[v] -= 1
        if indegree[v] == 0:
            stack.append(v)

for u in range(N):
    if parent[u] == u and indegree[u] > 0:
        print("inconsistent")
        exit(0)

print("consistent")