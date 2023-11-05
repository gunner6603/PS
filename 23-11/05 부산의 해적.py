# https://www.acmicpc.net/problem/2424

import sys
from collections import deque

inp = sys.stdin.readline

N, M = map(int, inp().split())
chart = [inp().rstrip() for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

sooa_loc = None
pirate_loc = None
for i, row in enumerate(chart):
    s_col = row.find("Y")
    p_col = row.find("V")
    if s_col != -1:
        sooa_loc = (i, s_col)
    if p_col != -1:
        pirate_loc = (i, p_col)

pirate_dist = [[float('inf')] * M for _ in range(N)]
mark = [[float('inf')] * M for _ in range(N)]

discovered = [[False] * M for _ in range(N)]
q = deque([(*pirate_loc, 0)])
discovered[pirate_loc[0]][pirate_loc[1]] = True
while q:
    ox, oy, d = q.popleft()
    pirate_dist[ox][oy] = d
    for k in range(4):
        nx = ox + dx[k]
        ny = oy + dy[k]
        if 0 <= nx < N and 0 <= ny < M and chart[nx][ny] != 'I' and not discovered[nx][ny]:
            discovered[nx][ny] = True
            q.append((nx, ny, d + 1))

for i in range(N):
    start = 0
    min_val = float('inf')
    for j in range(M + 1):
        if j == M or chart[i][j] == 'I':
            for k in range(start, j):
                mark[i][k] = min(mark[i][k], min_val)
            start = j + 1
            min_val = float('inf')
        else:
            min_val = min(min_val, pirate_dist[i][j])
    
for j in range(M):
    start = 0
    min_val = float('inf')
    for i in range(N + 1):
        if i == N or chart[i][j] == 'I':
            for k in range(start, i):
                mark[k][j] = min(mark[k][j], min_val)
            start = i + 1
            min_val = float('inf')
        else:
            min_val = min(min_val, pirate_dist[i][j]) 
            
for i in range(N):
    for j in range(M):
        mark[i][j] = max(1, mark[i][j])
            
discovered = [[False] * M for _ in range(N)]
q = deque([(*sooa_loc, 0)])
discovered[sooa_loc[0]][sooa_loc[1]] = True
success = False
while q:
    ox, oy, d = q.popleft()
    if chart[ox][oy] == 'T':
        success = True
        break
    for k in range(4):
        nx = ox + dx[k]
        ny = oy + dy[k]
        if 0 <= nx < N and 0 <= ny < M and chart[nx][ny] != 'I' and not discovered[nx][ny] and d + 1 < mark[nx][ny]:
            discovered[nx][ny] = True
            q.append((nx, ny, d + 1))

print("YES" if success else "NO")