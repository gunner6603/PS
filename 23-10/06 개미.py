# https://www.acmicpc.net/problem/14942

import sys
from collections import defaultdict
from bisect import bisect_left

inp = sys.stdin.readline

N = int(inp())
energy = [int(inp()) for _ in range(N)]
link = defaultdict(list)
visited = [-1] * N
stack = []

for _ in range(N - 1):
    u, v, w = map(int, inp().split())
    link[u - 1].append((v - 1, w))
    link[v - 1].append((u - 1, w))

def dfs(u, cur_sum):
    stack.append((cur_sum, u))
    idx = bisect_left(stack, (cur_sum - energy[u], 0))
    visited[u] = stack[idx][1]
    for v, w in link[u]:
        if visited[v] == -1:
            dfs(v, cur_sum + w)
    stack.pop()

dfs(0, 0)

for i in range(N):
    print(visited[i] + 1)