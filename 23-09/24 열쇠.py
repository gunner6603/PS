# https://www.acmicpc.net/problem/9328

import sys
from collections import defaultdict, deque

inp = sys.stdin.readline

T = int(inp())
DISCOVER_MARK = '@'
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

def move(i, j):
    global docs
    val = chart[i][j]
    if val == '.':
        chart[i][j] = DISCOVER_MARK
        queue.append((i, j))
    elif 'a' <= val <= 'z':
        chart[i][j] = DISCOVER_MARK
        keys[val] = True
        queue.append((i, j))
        for k, l in unopened[val]:
            queue.append((k, l))
    elif 'A' <= val <= 'Z':
        chart[i][j] = DISCOVER_MARK
        if keys[val.lower()]:
            queue.append((i, j))
        else:
            unopened[val.lower()].append((i, j))
    elif val == '$':
        chart[i][j] = DISCOVER_MARK
        docs += 1
        queue.append((i, j))
                 
for _ in range(T):
    H, W = map(int, inp().split())
    queue = deque()
    keys = defaultdict(bool)
    unopened = defaultdict(list)
    chart = [list(inp().rstrip()) for _ in range(H)]
    docs = 0
    
    for k in inp().rstrip():
        keys[k] = True
            
    for i in range(H):
        for j in range(W):
            if (i == 0 or i == H - 1) or (j == 0 or j == W - 1):
                move(i, j)
    
    while queue:
        ox, oy = queue.popleft()
        for k in range(4):
            nx = ox + dx[k]
            ny = oy + dy[k]
            if 0 <= nx < H and 0 <= ny < W and chart[nx][ny] not in ('*', '@'):
                move(nx, ny)
    
    print(docs)