# https://www.acmicpc.net/problem/1981

import sys
from collections import deque

inp = sys.stdin.readline

N = int(inp())
chart = [list(map(int, inp().split())) for _ in range(N)]
min_val = min(min(row) for row in chart)
max_val = max(max(row) for row in chart)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def filtered_bfs(lower_bound, upper_bound):
    discovered = [[False] * N for _ in range(N)]
    q = deque([(0, 0)])
    while q:
        ox, oy = q.popleft()
        if not (lower_bound <= chart[ox][oy] <= upper_bound):
            continue
        if ox == oy == N - 1:
            return True
        for i in range(4):
            nx = ox + dx[i]
            ny = oy + dy[i]
            if 0 <= nx < N and 0 <= ny < N and not discovered[nx][ny]:
                discovered[nx][ny] = True
                q.append((nx, ny))
    return False

left = 0
right = max_val - min_val
while left <= right:
    mid = (left + right) // 2
    for i in range(min_val, max_val + 1 - mid):
        if i <= chart[0][0] <= i + mid and i <= chart[N - 1][N - 1] <= i + mid:
            if filtered_bfs(i, i + mid):
                right = mid - 1
                break
    else:
        left = mid + 1

print(left)