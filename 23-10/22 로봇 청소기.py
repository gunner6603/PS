# https://www.acmicpc.net/problem/4991

import sys
from collections import deque

inp = sys.stdin.readline

def bfs(x, y):
    dist = [float('inf')] * dirty_cnt
    discovered = [[False] * w for _ in range(h)]
    q = deque([(x, y, 0)])
    discovered[x][y] = True
    while q:
        ox, oy, d = q.popleft()
        if room[ox][oy] == '*':
            dist[loc_to_idx[(ox, oy)]] = d
        for k in range(4):
            nx = ox + dx[k]
            ny = oy + dy[k]
            if 0 <= nx < h and 0 <= ny < w and room[nx][ny] != 'x' and not discovered[nx][ny]:
                discovered[nx][ny] = True
                q.append((nx, ny, d + 1))
    return dist

def dfs(cur, visited):
    if visited == all_set:
        return 0
    if dp[cur][visited] is not None:
        return dp[cur][visited]
    min_dist = float('inf')
    for nxt in range(dirty_cnt):
        if visited & (1 << nxt) == 0:
            d = dist_matrix[cur][nxt] + dfs(nxt, visited | (1 << nxt))
            min_dist = min(min_dist, d)
    dp[cur][visited] = min_dist
    return min_dist

while True:
    w, h = map(int, inp().split())
    if w == h == 0:
        break
    room = [list(inp().rstrip()) for _ in range(h)]
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    dirty_cnt = 0
    idx_to_loc = dict()
    loc_to_idx = dict()
    start_loc = None
    for i in range(h):
        for j in range(w):
            elem = room[i][j]
            if elem == "o":
                start_loc = (i, j)
            elif elem == "*":
                idx_to_loc[dirty_cnt] = (i, j)
                loc_to_idx[(i, j)] = dirty_cnt
                dirty_cnt += 1

    dist_matrix = [bfs(*idx_to_loc[i]) for i in range(dirty_cnt)]
    start_to_dirty_dist = bfs(*start_loc)
    dp = [[None] * 2**dirty_cnt for _ in range(dirty_cnt)]
    all_set = 2**dirty_cnt - 1
    
    min_dist = float('inf')
    for i in range(dirty_cnt):
        d = start_to_dirty_dist[i] + dfs(i, 1 << i)
        min_dist = min(min_dist, d)

    print(min_dist if min_dist != float('inf') else -1)