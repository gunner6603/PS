# https://www.acmicpc.net/problem/16724

import sys

inp = sys.stdin.readline

N, M = map(int, inp().split())
chart = [inp().rstrip() for _ in range(N)]
visited = [[False] * M for _ in range(N)]
indegree = [[0] * M for _ in range(N)]
directions = {
    'U' : (-1, 0),
    'D' : (1, 0),
    'L' : (0, -1),
    'R' : (0, 1) 
}

for ox in range(N):
    for oy in range(M):
        direction_key = chart[ox][oy]
        direction_value = directions[direction_key]
        nx = ox + direction_value[0]
        ny = oy + direction_value[1]
        indegree[nx][ny] += 1

stk = []
for i in range(N):
    for j in range(M):
        if indegree[i][j] == 0:
            stk.append((i, j))
            
while stk:
    ox, oy = stk.pop()
    visited[ox][oy] = True
    direction_key = chart[ox][oy]
    direction_value = directions[direction_key]
    nx = ox + direction_value[0]
    ny = oy + direction_value[1]
    indegree[nx][ny] -= 1
    if indegree[nx][ny] == 0:
        stk.append((nx, ny))
    
def dfs(ox, oy):
    visited[ox][oy] = True
    
    direction_key = chart[ox][oy]
    direction_value = directions[direction_key]
    nx = ox + direction_value[0]
    ny = oy + direction_value[1]
    if not visited[nx][ny]:
        dfs(nx, ny)

cnt = 0
for i in range(N):
    for j in range(M):
        if not visited[i][j]:
            dfs(i, j)
            cnt += 1

print(cnt)