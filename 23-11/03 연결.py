# https://www.acmicpc.net/problem/5022

from collections import deque

MIS = lambda: map(int,input().split())

N, M = MIS()

A1 = tuple(MIS())
A2 = tuple(MIS())
B1 = tuple(MIS())
B2 = tuple(MIS())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def bfs(discovered, A1, A2):
    q = deque([(*A1, 0)])
    discovered[A1[0]][A1[1]] = A1
    while q:
        ox, oy, d = q.popleft()
        if (ox, oy) == A2:
            return d
        for k in range(4):
            nx = ox + dx[k]
            ny = oy + dy[k]
            if 0 <= nx <= N and 0 <= ny <= M and not discovered[nx][ny]:
                discovered[nx][ny] = (ox, oy)
                q.append((nx, ny, d + 1))
                
    return float('inf')

def find(A1, A2, B1, B2):
    discovered = [[None] * (M + 1) for _ in range(N + 1)]
    discovered[B1[0]][B1[1]] = B1    
    discovered[B2[0]][B2[1]] = B2
        
    # A1에서 A2로 가는 최단 경로 구하기
    d1 = bfs(discovered, A1, A2)
    
    # 최단 경로를 구성하는 정점을 discovered에 표시하기
    cur = A2
    prev = discovered[cur[0]][cur[1]]
    while cur != prev:
        discovered[cur[0]][cur[1]] = (-1, -1)
        cur = prev
        prev = discovered[cur[0]][cur[1]]
    discovered[cur[0]][cur[1]] = (-1, -1)
    
    for i in range(N + 1):
        for j in range(M + 1):
            if discovered[i][j] != (-1, -1):
                discovered[i][j] = None
    
    # B1에서 B2로 가는 최단 경로 구하기
    d2 = bfs(discovered, B1, B2)
    
    # 두 최단 경로의 합을 반환하기
    return d1 + d2

min_val = min(find(A1, A2, B1, B2), find(B1, B2, A1, A2))
print(min_val if min_val < float('inf') else "IMPOSSIBLE")