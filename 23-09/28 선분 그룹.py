# https://www.acmicpc.net/problem/2162
# 17387(선분 교차 2) 코드 재사용

import sys
sys.setrecursionlimit(3000)

inp = sys.stdin.readline

def resolve_relative_pos(x1, y1, x2, y2, a, b):
    if x1 == x2:
        if a == x1:
            return 0
        elif a < x1:
            return 1
        else:
            return 2
    elif y1 == y2:
        if b == y1:
            return 0
        elif b < y1:
            return 1
        else:
            return 2
    else:
        if x1 > x2:
            x1, x2 = x2, x1
            y1, y2 = y2, y1
        val = (x2 - x1) * (b - y1) - (y2 - y1) * (a - x1)    
        if val == 0:
            return 0
        elif val < 0:
            return 1
        else:
            return 2

def cross_check(line1, line2):
    x1, y1, x2, y2 = line1
    x3, y3, x4, y4 = line2
    
    a = resolve_relative_pos(x1, y1, x2, y2, x3, y3)
    b = resolve_relative_pos(x1, y1, x2, y2, x4, y4)
    c = resolve_relative_pos(x3, y3, x4, y4, x1, y1)
    d = resolve_relative_pos(x3, y3, x4, y4, x2, y2)

    cross = True

    if a == b and a != 0:
        cross = False
    elif c == d and c != 0:
        cross = False
    if a == b == 0:
        points = [(x1, y1, 0), (x2, y2, 0), (x3, y3, 1), (x4, y4, 1)]
        points.sort()
        if points[0][2] == points[1][2] and points[1][:2] != points[2][:2]:
            cross = False
            
    return cross

def dfs(u):
    global size
    visited[u] = True
    size += 1
    for v in links[u]:
        if not visited[v]:
            dfs(v)
    
N = int(inp())
lines = [list(map(int, inp().split())) for _ in range(N)]
links = [[] for _ in range(N)]
visited = [False] * N
group_cnt = 0
max_size = 0

for i in range(N):
    for j in range(i + 1, N):
        if cross_check(lines[i], lines[j]):
            links[i].append(j)
            links[j].append(i)
            
for i in range(N):
    if not visited[i]:
        group_cnt += 1
        size = 0
        dfs(i)
        max_size = max(max_size, size)

print(group_cnt)
print(max_size)