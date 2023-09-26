import sys
sys.setrecursionlimit(10**6)

inp = sys.stdin.readline

N, M = map(int, inp().split())

chart = [list(map(int, list(inp().rstrip()))) for _ in range(N)]
wall_cnt = [[0] * M for _ in range(N)]
visited = [[False] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def dfs(ox, oy):
    global zero_cnt
    zero_cnt += 1
    visited[ox][oy] = True
    for k in range(4):
        nx = ox + dx[k]
        ny = oy + dy[k]
        if 0 <= nx < N and 0 <= ny < M:
            if not visited[nx][ny]:
                if chart[nx][ny] == 0:
                    dfs(nx, ny)                
                else:
                    visited[nx][ny] = True
                    walls.append((nx, ny))
                    
for i in range(N):
    for j in range(M):
        if chart[i][j] == 0 and not visited[i][j]:
            zero_cnt = 0
            walls = []
            dfs(i, j)
            for x, y in walls:
                visited[x][y] = False
                wall_cnt[x][y] += zero_cnt
                wall_cnt[x][y] %= 10

for i in range(N):
    for j in range(M):
        wall_cnt[i][j] = (wall_cnt[i][j] + chart[i][j]) % 10
    print("".join(map(str, wall_cnt[i])))